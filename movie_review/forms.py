from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from movie_review.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exists")

    def validate_email(self, email):
        get_email = User.query.filter_by(email=email.data).first()
        if get_email:
            raise ValidationError("Email already exists")


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember Password')
    submit = SubmitField('Login')


class ReviewForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired()])
    movie_name = StringField('Movie name',
                             validators=[DataRequired()])
    rate = IntegerField('Rate',
                        validators=[DataRequired(), NumberRange(max=5, min=0)])
    content = TextAreaField('Review Content',
                            validators=[DataRequired()])
    submit = SubmitField('Submit')
