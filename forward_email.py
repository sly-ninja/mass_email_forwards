import input_prompts as pwd

import smtplib, imaplib, email

imap_host = "imap.gmail.com"
imap_port = 993
smtp_host = "smtp.gmail.com"
smtp_port = 587


user = pwd.USER
passwd = pwd.PASSWORD
from_addr = pwd.USER
to_addr = pwd.TO_EML
folder = pwd.FOLDER
   

def fetch_email():
    messages = []
    

    client = imaplib.IMAP4_SSL(imap_host, imap_port)
    client.login(user, passwd)
    client.select(folder)

    resp, data = client.search(None, 'ALL')
    if resp != 'OK':
        print('no messages found')
        return

    for i in data[0].split():
        resp, data = client.fetch(i, '(RFC822)' )
        if resp != 'OK':
            print("ERROR getting message", i)
            return
        
        # create a Message instance from the email data
        msg = email.message_from_bytes(data[0][1])
        # replace headers (could do other processing here)
        msg.replace_header("From", from_addr)
        msg.replace_header("To", to_addr)
        messages.append(msg)
#        
    client.close()
    client.logout()
    
    return messages


def forward_email():

    # open authenticated SMTP connection and send message with
    # specified envelope from and to addresses
    smtp = smtplib.SMTP(smtp_host, smtp_port)
    smtp.starttls()
    smtp.login(user, passwd)
    for message in messages:
        smtp.sendmail(from_addr, to_addr, message.as_string())
    smtp.quit()
    
    
messages = fetch_email()
forward_email()
