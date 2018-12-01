import config
import smtplib
import weatherpy

def send_email():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(config.EMAIL_ADDRESS, config.PASSWORD)
    message = 'Subject: Weather\n\n{}'.format(weatherpy.text)
    server.sendmail(config.EMAIL_ADDRESS, 'sean.boothby@gmail.com', message)
    server.quit()
    print("Success on sending email")
    




send_email()

