from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo,Email, length
from flask_wtf import FlaskForm

class SignupForm(FlaskForm):
    username = StringField("UserName", validators=[DataRequired()], _name="username")
    email = StringField("Email", validators=[DataRequired(), Email()], _name="email")
    password = PasswordField("Password", validators=[DataRequired()], _name="password")
    confirm_pass = PasswordField("Confirm Password", validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(), Email()], _name="email")
    password = PasswordField("Password", validators=[DataRequired()], _name="password")
    submit = SubmitField("Submit")

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired(), length(max=300) ])
    submit = SubmitField("Submit")
