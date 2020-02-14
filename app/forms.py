from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    """Contact form."""
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject= StringField('Subject', [DataRequired()])
    message = TextAreaField('Message', [DataRequired(),
