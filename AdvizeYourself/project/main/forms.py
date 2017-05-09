# project/main/forms.py


from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email, length, EqualTo


class SignUpForm(Form):
    email = TextField(
        'Enter your email address',
        validators=[DataRequired(), Email(), length(min=3)])
    password = PasswordField('Password', [DataRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')

