import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import sys
import os
import datetime


def send_attachment(recipient, subject, body, files=[]):
    assert type(recipient)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = COMMASPACE.join(recipient)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(body))

    for file in files:
        try:
            part = MIMEBase('application', "octet-stream")
            with open(file, 'rb') as fp:
                part.set_payload(fp.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            msg.attach(part)
        except:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(user, passwd)
            s.sendmail(user, recipient, msg.as_string())
            s.close()
        print("Email sent!")
        s.quit()
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise
    
    

user = ''
passwd = ''

#send_attachment( [recipient], subject, body, [attach] )
send_attachment(['name@domain.com'], 
         'Subject', 
         'Dear sir..', 
         ['tkinter_gui.py'] )



if __name__ == '__main__':
    send_attachment()