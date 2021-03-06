from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, IntegerField, SelectField, DateTimeField, BooleanField, validators

class UserForm(Form):
    email = TextField('Email', validators=[validators.Required()])
    fullname = TextField('Fullname', validators=[validators.Required()])


class UserRegistrationForm(UserForm):
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')


class UserEditForm(UserForm):
    score = IntegerField('Score', validators=[validators.InputRequired()])


class GameResultForm(Form):
    team_host_goals = IntegerField('Team Host goals', validators=[validators.InputRequired()], default=0)
    team_guest_goals = IntegerField('Team Guest goals', validators=[validators.InputRequired()], default=0)


class GameForm(Form):
    team_1 = SelectField(u'Host team', description='Host team', coerce=int)
    team_2 = SelectField(u'Guest team', description='Guest team', coerce=int)
    date = DateTimeField(u'Date', description='Date time in UTC')