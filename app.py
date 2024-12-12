from flask import Flask, render_template, request, redirect, url_for
from send_email import send_email
from telegram_test import telegram_test
from android_test import android_test
from ios_test import ios_test
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test/telegram', methods=['GET', 'POST'])
def test_telegram():
    if request.method == 'POST':
        api_id = request.form['api_id']
        api_hash = request.form['api_hash']
        bot_username = request.form['bot_username']
        admin_email = request.form['admin_email']
        image_path = request.form['image_path']

        telegram_test(api_id, api_hash, bot_username, admin_email, image_path)
        return redirect(url_for('index'))   
    return render_template('telegram_test.html')

@app.route('/test/android', methods=['GET', 'POST'])
def test_android():
    if request.method == 'POST':
        device_name = request.form['device_name']
        app_package = request.form['app_package']
        app_activity = request.form['app_activity']
        image_path = request.form['image_path']
        admin_email = request.form['admin_email']
        
      
        android_test(device_name, app_package, app_activity, image_path, admin_email)
        return redirect(url_for('index'))
    
    return render_template('android_test.html')

@app.route('/test/ios', methods=['GET', 'POST'])
def test_ios():
    if request.method == 'POST':
        app_path = request.form['app_path']
        image_path = request.form['image_path']
        admin_email = request.form['admin_email']
        

        ios_test(app_path, image_path, admin_email)
        return redirect(url_for('index'))  
    return render_template('ios_test.html')

if __name__ == '__main__':
    app.run(debug=True)
