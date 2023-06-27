import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#defines a function called send_email that uses the email and smtplib modules to send an email message via a Gmail account.
def send_email(subject, message, from_email, to_email, password):
    # Create a message object
    msg = MIMEMultipart()
    #an email message object is created and configured with the appropriate headers and message body. 
    # Set the subject and sender of the email
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    # Add the message body to the email
    msg.attach(MIMEText(message, 'plain'))

    # Create a SMTP server object and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()


subject = 'Stock Stimulator Team 3'
message = 'Thank you for using our stock simulator'
from_email = 'stockstimulator2023@gmail.com'
to_email = 'luongdminh183@gmail.com'
password = 'tllqnckhpnjuqgrt'

send_email(subject, message, from_email, to_email, password)
#an SMTP server object is created and used to send the email message. 
#the function is called with sample arguments to send an email with a specific 
#subject and message to a specific email address from a specific email account using a specific password.