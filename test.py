# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='vfcloud@vfgqacoe.com',
    to_emails='ashutosh.pandey@vodafone.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
