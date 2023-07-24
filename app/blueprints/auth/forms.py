from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp


class SignInForm(FlaskForm):
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired(),
                                        Regexp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", message='Must contain at least one of each of the following and be at least 8 characters long.<br>A-Z<br>a-z<br>0-9<br>#?!@$%^&*-')])
    submit = SubmitField('Sign In')



class SignUpForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired()])
    email = StringField('Email',
                            validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired(),
                                        Regexp("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", message='Must contain at least one of each of the following and at least 8 characters long.<br>A-Z<br>a-z<br>0-9<br>#?!@$%^&*-')])
    password2 = PasswordField('Confirm Password ',
                            validators=[DataRequired(),
                                        EqualTo('password', message='Your passwords did not match, please try again.')])
    submit = SubmitField('Sign Up')