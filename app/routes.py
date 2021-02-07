from app import app
from flask import render_template, request, jsonify
import json
import requests
import os


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/test', methods=['GET'])
def test():
    return os.environ.get("VAULT_ID")


@app.route('/add_message', methods=['POST'])
def add_message():
    card_number = request.form['card_number']
    exp_date = request.form['exp_date']
    cvv = request.form['cvv']
    res = requests.post(f'https://{os.environ.get("VAULT_ID")}.SANDBOX.verygoodproxy.com/post',
                        json={'card_number': card_number, 'exp_date': exp_date, 'cvc': cvv})

    data = json.loads(res.text) # this is a dict
    card_alias = data['json']['card_number'] # Acess aliased card number token in response
    exp_alias = data['json']['exp_date'] # Acess aliased exp date token in response
    cvv_alias = data['json']['cvc'] # Acess aliased cvc token in response
    return render_template('message.html', card_number=card_number, exp_date=exp_date, cvv=cvv, card_alias=card_alias, exp_alias=exp_alias, cvv_alias=cvv_alias)


@app.route('/forward', methods=['POST'])
def forward():
    card_number = request.form['card_number']
    exp_date = request.form['exp_date']
    cvv = request.form['cvv']

    os.environ['HTTPS_PROXY'] = f'https://{os.environ.get("HTTPS_PROXY_USERNAME")}:{os.environ.get("HTTPS_PROXY_PASSWORD")}@{os.environ.get("VAULT_ID")}.sandbox.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                        json={'card_number': card_number, 'exp_date': exp_date, 'cvc': cvv},
                        verify=f'{os.environ.get("CERT_PATH")}')

    res = res.json()
    return render_template('forward.html', response=res)