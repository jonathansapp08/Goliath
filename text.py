import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_text(email, pas, sms_gateway):  
    email = email
    pas = pas
    sms_gateway = sms_gateway

    # The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
    # and port is also provided by the email provider.
    smtp = "smtp.gmail.com" 
    port = 587
    # This will start our email server
    server = smtplib.SMTP(smtp,port)
    # Starting the server
    server.starttls()
    # Now we need to login
    server.login(email,pas)

    sms = "Check your game"

    server.sendmail(email,sms_gateway,sms)

    # lastly quit the server
    server.quit()
