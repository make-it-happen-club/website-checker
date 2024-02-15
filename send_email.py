# import packages
# below packages are built-in - no need to install anything new!
# yupi :)
import smtplib
from email.message import EmailMessage
import os

# set your email and password
# please use App Password
email_address = os.environ.get('FROM_EMAIL_ADDRESS')
email_password = os.environ.get('EMAIL_PASSWORD')
to_email_address = os.environ.get('TO_EMAIL_ADDRESS')



def send_email(failed_links):

    nl = '\n'
    subject = "Some links are not working properly"
    message = f"The following links returned status codes other than 200:\n\n{nl.join(failed_links)}"

    # create email
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to_email_address
    msg.set_content(message)
    
    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        print(f"Email sent")