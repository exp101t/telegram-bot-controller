from classes import db, User
from config import SALT

from hashlib import scrypt

username = input('Enter administrator username: ')
password = input('Enter administrator password: ')

hash = hashlib.scrypt(password.encode(), salt = SALT, n = 16384, r = 8, p = 1).hex()
user = User(username = username, password = hash)

db.create_all()
db.session.add(user)
db.session.commit()