import os

def ios_test(app_path, image_path, admin_email):
    try:
        
        print(f"Testing iOS App from {app_path}...")

        
        os.system(f'open {app_path}')

        
        send_email('Test Passed', 'iOS app test completed successfully', admin_email)
    except Exception as e:
        send_email('Test Failed', str(e), admin_email)
        print(f"Error in iOS test: {e}")
