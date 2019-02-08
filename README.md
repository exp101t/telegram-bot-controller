# Telegram Bot Controller
## Running the server
Firstly, `config.py` must contain something like this:
```
from classes import app

USE_PROXY  = True
PROXY_IP   = '1.2.3.4'
PROXY_PORT = 4321

SALT = b'CHANGEMEPLEASE'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bots.db'
app.config['SECRET_KEY'] = 'CHANGEMEPLEASE'
```
Secondly, lets install python requirements:
```
$ pip3 install -r requirements.txt
```
Thirdly, lets initialise database and enter admin login and password:
```
$ python3 init_database.py
```
Now, your system is ready to run the server. Just execute following command:
```
$ python3 server.py
```
**P.S. It is highly recommended** to use random byte strings for app secret key and scrypt salt. You can generate it using Python:
```
import os
os.urandom(32)
```
## To Do
- [X] Create login page
- [ ] Attachments for messages
- [X] Add logout button and link to admin page
- [ ] Add multiuser system
- [ ] Chat with people through a bot