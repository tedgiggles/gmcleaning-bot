from flask import Flask, request
import requests

app = Flask(__name__)

# 🔐 Токен и Chat ID
TELEGRAM_TOKEN = '7207668599:AAEwnxvirQz6qf2YGFG0PULCwgmU8HnzgDU'
CHAT_ID = '5945413679'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Пытаемся получить JSON (используется CF7 to Webhook)
        data = request.get_json(force=True)
    except:
        # Если не JSON — читаем как form-data
        data = request.form

    # Для отладки (можно удалить после проверки)
    print('📨 От формы получены данные:', data)

    # Получаем имя и телефон (названия должны совпадать с полями формы)
    name = data.get('your-name', 'Без імені')
    phone = data.get('your-phone', 'Без телефону')

    # Готовим сообщение
    message = f'📥 Нова заявка з сайту:\n👤 Імʼя: {name}\n📞 Телефон: {phone}'

    # Отправка в Telegram
    send_to_telegram(message)

    return 'OK', 200

def send_to_telegram(text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text
    }
    response = requests.post(url, data=payload)
    print('📤 Telegram response:', response.text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
