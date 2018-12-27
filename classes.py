import flask, flask_sqlalchemy

from flask_login import LoginManager, UserMixin, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm

app = flask.Flask(__name__)
db  = flask_sqlalchemy.SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class LoginForm(FlaskForm):
    username = StringField('Login', validators = [InputRequired()])
    password = PasswordField('Password', validators = [InputRequired()])

class Bot(db.Model):
    id    = db.Column(db.Integer, primary_key = True)
    name  = db.Column(db.String(20))
    token = db.Column(db.String(50))

class Chat(db.Model):
    uid  = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    id   = db.Column(db.Integer)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(128))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class IndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

admin = Admin(app, index_view = IndexView())
admin.add_view(AdminView( Bot, db.session))
admin.add_view(AdminView(Chat, db.session))
admin.add_view(AdminView(User, db.session))