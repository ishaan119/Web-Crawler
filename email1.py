import smtplib
from email.MIMEText import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess
import shelve

def getPubIp():
        pipe = subprocess.Popen(["curl", "ipecho.net/plain"],stdout=subprocess.PIPE)
        pubIp = pipe.stdout.read()
        return  pubIp

def sendEmail(text,user,password,toEmail,fromEmail,subject='testEmail'):
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    #Connecting to the Gmail server
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    #Making sure we encrypt username and password while sending data
    server.starttls()
    server.ehlo()
    server.login(user, password)
    server.sendmail(fromEmail, toEmail,msg.as_string())
    server.quit()
    return "Email sent"


def main():
    j = getPubIp()
    print j
    k = sendEmail(j,'ishaansutaria','bdayishaan','ishaan.sutaria@aylanetworks.com','ishaansutaria@gmail.com')
    print k


if __name__ == "__main__":main()


