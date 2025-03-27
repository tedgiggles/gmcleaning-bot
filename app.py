from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = '7207668599:AAEwnxvirQz6qf2YGFG0PULCwgmU8HnzgDU'
CHAT_ID = '5945413679'


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.form
    name = data.get('your-name', 'Без імені')
    phone = data.get('your-phone', 'Без телефону')

    message = f'📥 Нова заявка з сайту:\n👤 Імʼя: {name}\n📞 Телефон: {phone}'

    send_to_telegram(message)
    return 'OK', 200


def send_to_telegram(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }
    requests.post(url, data=payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
