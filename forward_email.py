import passwords as pwd

import smtplib, imaplib, email

imap_host = "imap.gmail.com"
imap_port = 993
smtp_host = "smtp.gmail.com"
smtp_port = 587


user = pwd.USER
passwd = pwd.PASSWORD
from_addr = pwd.FROM_EML
to_addr = pwd.TO_EML

   
    

def fetch_email():
    messages = []
    
    try:
        client = imaplib.IMAP4_SSL(imap_host, imap_port)
        client.login(user, passwd)
        client.select('rastabus')

        type, data = client.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        last_email_id = int(id_list[-1])



        for i in range(last_email_id, first_email_id, -1):
            typ, data = client.fetch(i, '(RFC822)' )
        
            for response_part in data:
                if isinstance(response_part, tuple):
                # create a Message instance from the email data
                    msg = email.message_from_string(response_part[1])
                # replace headers (could do other processing here)
                    msg.replace_header("From", from_addr)
                    msg.replace_header("To", to_addr)
                    messages.append(msg)
            
        client.close()
        client.logout()
        
        return messages

    except:
        raise Exception
        print('SOMETHING')



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
