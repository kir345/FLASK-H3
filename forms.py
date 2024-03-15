from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    parole = PasswordField('Parole', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    parole = PasswordField('Parole', validators=[DataRequired(), Length(min=8)])
    confirm_par = PasswordField('Parole', validators=[DataRequired(), EqualTo('parole')])