import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def SendEmailAttch(ToEmail):
    MyEmail = "kalathilabhijeet10@gmail.com"
    MyPassword = "Password"
    fromaddr = MyEmail
    toaddr = ToEmail
    print("before deatisl")
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Processs Information Log"
    body = "Hi, This is test email for Processs Information Log"

    msg.attach(MIMEText(body, 'plain'))

    filename = "Log.txt"
    attachment = open("Demo\Log.txt", "rb")

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(p)
    print("Before session")
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, MyPassword)
    print("after session")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
