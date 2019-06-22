from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '7ba020549b38ee7b7c013e869fc8570d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://yibckngauklqvf:7f880412186151edafbf4b26ec787719dc554cdc97a938dd87af9b185ad2265a@ec2-50-19-254-63.compute-1.amazonaws.com:5432/ddcj1n79249i44'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
