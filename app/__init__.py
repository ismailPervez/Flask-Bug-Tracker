from flask import Flask

app = Flask(__name__)

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .models import User, db
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from flask_login import LoginManager

mail = Mail()
login = LoginManager()

app = Flask(__name__)

load_dotenv('.env')
app.config.from_pyfile('config.py')

migrate = Migrate(app, db)

db.init_app(app)
db = SQLAlchemy(app)

login.init_app(app)
login.login_view = 'login'

mail.init_app(app)
bcrypt = Bcrypt(app)

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from app import views