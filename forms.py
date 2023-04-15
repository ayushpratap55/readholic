from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Length, EqualTo, DataRequired

class dminRegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PassswordField("Password", validators=[DataRequired(), Length(min=6)])
    conform_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])


    submit = SubmitField("Register")

class dminRegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PassswordField("Password", validators=[DataRequired(), Length(min=6)])

    submit = SubmitField("Login")