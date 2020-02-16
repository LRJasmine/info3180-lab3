from flask import Flask
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SECRET_KEY'] = 'vgy67gg@ffRRt'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465' # (or try 2525)
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''

#csrf.init_app(app)
csrf = CSRFProtect(app)

mail = Mail(app)
from app import views
csrf = CSRFProtect(app)
