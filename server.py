from classes import db, app, Bot, User
from flask import render_template, request, jsonify
import config, requests
from config import PROXY_IP, PROXY_PORT

API_URL = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=html'

@app.route('/')
def index():
    return render_template('controlpanel.html', bots = Bot.query.all(), users = User.query.all())

@app.route('/send', methods = ['POST'])
def send_message():
    try:
        user_id = int(request.form.get('user_id', 0))
        bot_id  = int(request.form.get('bot_id', 0))
        text    = request.form.get('text', '')
    except:
        return jsonify({'successful': False, 'reason': 'Incorrect user or bot ID'}), 400
    
    try:
        proxy_dict = {'https': 'https://%s:%s' % (PROXY_IP, PROXY_PORT)}
        
        bot_token = Bot.query.filter_by(id = bot_id).one().token
        user_id   = User.query.filter_by(uid = user_id).one().id

        requests.get(API_URL % (bot_token, user_id, text), proxies = proxy_dict)
        return jsonify({'successful':  True}), 200
    except:
        return jsonify({'successful': False, 'reason': 'Proxy is unavailable or bot or user ID is incorrect'}), 400

if __name__ == '__main__':
    app.run(debug = True)
