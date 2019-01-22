from classes import app, Bot, Chat, User, LoginForm
from config import PROXY_IP, PROXY_PORT, SALT

from flask import render_template, request, jsonify, redirect
import requests, flask_login, hashlib

API_URL = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=html'

def login_required(func):
    def wrapper():
        if flask_login.current_user.is_authenticated:
            return func()
        else: return redirect('/login')

    # Thanks Roei Bahumi (https://stackoverflow.com/questions/17256602/)
    wrapper.__name__ = func.__name__
    return wrapper

@app.route('/')
@login_required
def index():
    return render_template('controlpanel.html', bots = Bot.query.all(), users = Chat.query.all())

@app.route('/send', methods = ['POST'])
@login_required
def send_message():
    try:
        user_id = int(request.form.get('user_id', 0))
        bot_id  = int(request.form.get('bot_id', 0))
        text    = request.form.get('text', '')
    except:
        return jsonify({'successful': False, 'reason': 'Incorrect user or bot ID'}), 200
    
    try:
        proxy_dict = {'https': 'https://%s:%s' % (PROXY_IP, PROXY_PORT)}
        
        bot_token = Bot.query.filter_by(id = bot_id).one().token
        user_id   = Chat.query.filter_by(uid = user_id).one().id

        requests.get(API_URL % (bot_token, user_id, text), proxies = proxy_dict)
        return jsonify({'successful':  True}), 200
    except:
        return jsonify({'successful': False, 'reason': 'Proxy is unavailable or bot or user ID is incorrect'}), 200

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        hash = hashlib.scrypt(form.password.data.encode(), salt = SALT, n = 16384, r = 8, p = 1).hex()

        if isinstance(user, type(None)) or hash != user.password:
            return render_template('loginpage.html', form = form, error = 'Incorrect login or password')

        flask_login.login_user(user)
        return redirect('/')
    return render_template('loginpage.html', form = form)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)