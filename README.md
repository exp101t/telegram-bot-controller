# Telegram Bot Controller
## Running the server
Firstly, lets install python requirements:
```
$ pip3 install -r requirements.txt
```
Secondly, lets initialise database:
```
$ python3 init_database.py
```
Now, your system is ready to run the server. Just execute following command:
```
$ python3 server.py
```
**P.S.** `config.py` must contain something like this:
```
from classes import app

PROXY_IP   = '1.2.3.4'
PROXY_PORT = 4321

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bots.db'
app.config['SECRET_KEY'] = 'CHANGEMEPLEASE'
```
If you don't want to use proxy, you can just delete `proxies` parameter in requests.get call in `server.py`.
## To Do
There is nothing. It will be updated soon.
