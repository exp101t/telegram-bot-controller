from classes import db
import config

db.create_all()
db.session.commit()