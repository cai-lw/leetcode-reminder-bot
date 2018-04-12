# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

def notify_by_email(user, email):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ['SENDGRID_API_KEY'])
    from_email = Email('noreply@leetcode-reminder-bot.org')
    to_email = Email(email)
    subject = 'You have not solved any problem on Leetcode for a day!'
    content = Content('text/plain', open('email.txt').read().format(user=user))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print("Sent email to %s\'s email %s. Status code: %d." % (user, email, response.status_code))
    return response