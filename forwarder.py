import smtplib, imaplib, email, os

imap_host = "imap.gmail.com"
imap_port = 993
smtp_host = "smtp.gmail.com"
smtp_port = 587
client = imaplib.IMAP4_SSL(imap_host, imap_port)

def forward_emails():
    yes = set(['yes','y', 'ye', ''])
    
    user = input('Please enter your email address: ')
    passwd = input('Please enter your password: ')
    recipient = input("Please enter the recipient's email address: ")
    folder = input('Please enter the name of the gmail folder you would like to forward: ')
 
    try:
        client.login(user, passwd)
    except:
        print('\n', 'login failed')
        
        choice = input('Would you like to quit? ')
        if choice in yes:
            os._exit(0)
        else:
            forward_emails()

    
    client.select(folder)
    resp, data = client.search(None, 'ALL')
    if resp != 'OK':
        print('no messages found')
        return

    messages = []
    for i in data[0].split():
        resp, data = client.fetch(i, '(RFC822)' )
        if resp != 'OK':
            print("ERROR getting message", i)
            return
        
        msg = email.message_from_bytes(data[0][1])
        msg.replace_header("From", user)
        msg.replace_header("To", 'sylviaxh@gmail.com')
        messages.append(msg)
        
    client.close()
    client.logout()
    
    smtp = smtplib.SMTP(smtp_host, smtp_port)
    smtp.starttls()
    smtp.login(user, passwd)
    for message in messages:
        smtp.sendmail(user, recipient, message.as_string())
    smtp.quit()
    
    return True

forward_emails()