import requests

def telegram_test(api_id, api_hash, bot_username, admin_email, image_path):
    # Logic to send Telegram message or execute Telegram Bot actions
    try:
        # Assuming this function sends a test message to Telegram Bot
        url = f'https://api.telegram.org/bot{api_id}:{api_hash}/sendPhoto'
        params = {
            'chat_id': bot_username,
            'photo': image_path,
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            print('Telegram test successful')
        else:
            print('Telegram test failed')
            send_email('Test Failed', 'Telegram bot test failed', admin_email)
    except Exception as e:
        send_email('Test Failed', str(e), admin_email)
        print(f"Error in Telegram test: {e}")
