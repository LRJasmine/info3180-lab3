from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, validators
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject= StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])