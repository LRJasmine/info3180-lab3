from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject= StringField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired(),
