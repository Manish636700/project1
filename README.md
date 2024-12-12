# Test Automation Dashboard with Email and Telegram Notifications

Overview:
This project is a web-based dashboard built using Flask, designed to manage and execute automated tests for different systems (Telegram bot, Android app, iOS app). The dashboard provides an interface where users can trigger different types of tests by submitting relevant details, such as API credentials, app paths, and device configurations. After the test is executed, if any test fails, the system will automatically send email notifications to the specified admin email. Additionally, for the Telegram bot test, users can receive real-time updates through Telegram notifications.

#Key Features:
Web Interface (Dashboard):

A simple dashboard where users can select and trigger tests for Telegram bot, Android apps, and iOS apps.
Users can input necessary test parameters (e.g., API credentials, app paths, etc.) via forms in the web interface.
Test Cases:

Telegram Bot Test: Users can test Telegram bots by providing API credentials and image paths. The bot can be used to send a message or test other functionality. If the test fails, an email notification is sent to the admin.
Android App Test: Users can run a test on an Android app by providing the device name, app package, and activity. The system will trigger an Android test using adb (Android Debug Bridge) commands. If the test fails, an email is sent to the admin.
iOS App Test: Similar to the Android app test, users can trigger a test for an iOS app by providing the app path and necessary image paths. If the test fails, an email is sent to the admin.
Email Notifications:

Email notifications are sent whenever a test fails, informing the admin about the failure and providing details about the error.
The system uses SMTP to send emails to the admin, which can be configured with the sender's email and password.
Telegram Notifications (for Telegram Bot Test):

For the Telegram bot test, if the test is successful or fails, the admin can also receive a Telegram notification. This feature is particularly useful for real-time updates.
The Telegram bot sends updates to a specified Telegram chat (admin or group chat), using the provided API credentials.
Form-based Configuration:

The forms on the web interface take input such as API keys, device names, app paths, and admin emails.
Once submitted, the backend runs the corresponding test case and provides feedback via email and Telegram.



#Technology Stack:
Backend:

Flask: A lightweight web framework used to build the backend of the dashboard. Flask is used for routing requests and rendering HTML templates.
Python: The primary programming language used for writing backend logic and handling test executions.
Frontend:

HTML: Basic HTML forms are used for user input (e.g., API keys, image paths, etc.).
CSS/Bootstrap: Simple styling to enhance the user interface (optional).
Test Execution:

Telegram Bot Test: Uses the Telegram API to interact with the bot and send messages/photos to verify its functionality.
Android App Test: Uses adb (Android Debug Bridge) commands to interact with Android devices and run app-related tests.
iOS App Test: Executes iOS tests, potentially using Xcode or Appium (or custom scripts for iOS).
Email Notifications:

SMTP: For sending email notifications in case of test failures.
Python smtplib: To send email notifications to the admin when a test fails.
Telegram Notifications:

Python requests: To interact with Telegram’s API and send messages or images to a designated chat.
