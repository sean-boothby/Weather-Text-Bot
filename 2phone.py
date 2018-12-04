import config
import smtplib
import weatherpy

names = []
emails = []

def send_email():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(config.EMAIL_ADDRESS, config.PASSWORD)
    for name in range(len(names)):
        FNAME, LNAME, email = config.name(names[name],emails[name])
        text = message(FNAME,LNAME)
        server.sendmail(email, 'sean.boothby@gmail.com', text)
    server.quit()
    print("Success on sending emails")

def message(FNAME,LNAME):
    ## Later add feature to take input to determine which API to make message from
    subject = 'Subject: Weather Updates for you ' + LNAME + '\n\n'
    message = weatherpy.checkweather(config.API_KEY)
    message = FNAME + 'you are a giant BAMF.\n\n' + message
    message = subject + message
    return message



send_email()

