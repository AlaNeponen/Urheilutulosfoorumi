from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=2, max=25), validators.Regexp('.*\w+.*', message='Must contain characters and/or numbers')])
    password = PasswordField("Password", [validators.Length(min=6, max=140), validators.Regexp('.*\w+.*', message='Must contain characters and/or numbers')])

    class Meta:
        csrf = False