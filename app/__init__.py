from flask import Flask
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vgy67gg@ffRRt'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = '17868b07c5e498'
app.config['MAIL_PASSWORD'] = 'd46fbde47eb103'

mail = Mail(app)
from app import views