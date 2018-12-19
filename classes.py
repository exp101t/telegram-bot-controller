from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import flask, flask_sqlalchemy

app = flask.Flask(__name__)
db  = flask_sqlalchemy.SQLAlchemy(app)

class Bot(db.Model):
    id    = db.Column(db.Integer, primary_key = True)
    name  = db.Column(db.String(20))
    token = db.Column(db.String(50))
    
class User(db.Model):
    uid  = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    id   = db.Column(db.Integer)
    
admin = Admin(app)
admin.add_view(ModelView( Bot, db.session))
admin.add_view(ModelView(User, db.session))