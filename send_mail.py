import smtplib

fromaddr = 'openpubg@gmail.com'
toaddrs  = '5182483322@mms.att.net'
msg = 'text_body'

def sendEmail():
    # Credentials (if needed)
    username = 'openpubg@gmail.com'
    password = 'blackglasses'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()