import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_USER = 'mail@gmail.com'
EMAIL_PASSWORD = 'mtso vrgm nuez zpuq'
TO_EMAIL = 'mymail@gmail.com'
SUBJECT = 'Daily Report'

def send_email():
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT

    # Email body
    body = 'This is your daily report.'
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the server
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        server.quit()

# Schedule the email to be sent daily at a specific time (e.g., 24:00)
schedule.every().day.at('20:42').do(send_email)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait a minute before checking the schedule again
