import os

def android_test(device_name, app_package, app_activity, image_path, admin_email):
    try:
        
        print(f"Testing Android App {app_package} on {device_name}...")

        os.system(f'adb -s {device_name} shell am start -n {app_package}/{app_activity}')

        send_email('Test Passed', 'Android app test completed successfully', admin_email)
    except Exception as e:
        send_email('Test Failed', str(e), admin_email)
        print(f"Error in Android test: {e}")
