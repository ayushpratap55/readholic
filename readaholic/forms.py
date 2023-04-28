from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FloatField, TextAreaField,FileField
from wtforms.validators import Email, Length, EqualTo, DataRequired, NumberRange

class AdminRegistrationForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Register")

class AdminLoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    submit = SubmitField("Login")

class AddBookForm(FlaskForm):
    book_title = StringField(
        label="Title", validators=[DataRequired(), Length(max=120)]
    )
    author_name = StringField(
        label="Author", validators=[DataRequired(), Length(max=40)]
    )
    cover_image_file = FileField(label="Upload Cover Image")
    isbn = StringField(label="ISBN", validators=[DataRequired()])
    genre = SelectField(label="Genre", choices=[('book1','Choose...'),('book2','Mystery'),('book3','Fiction'),('book3','Education')])
    rating = FloatField(label="Rating", validators=[NumberRange(min=0, max=5)])
    shop_link = StringField(label="Shop Link")
    tiny_summary = TextAreaField(
        label="Tiny Summary",
        validators=[DataRequired()],
        render_kw={"placeholder": "few words ..."},
    )
    submit = SubmitField(label="Save")
