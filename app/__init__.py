from flask_wtf.csrf import CSRFProtect
from flask import Flask
from flask_mail import Mail
from app import views


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vgy67gg@ffRRt'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''

mail = Mail(app)
csrf = CSRFProtect(app)
