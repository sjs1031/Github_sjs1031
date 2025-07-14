# The email / smtplib Module

# Email Basic - How to Send an Email with smtplib
import smtplib
HOST = "mySMTP.server.com"
SUBJECT = "Test email from Python"
TO = "sjs1031@gmail.com"
FROM = "python@rulexuan.kr"
text = "Python 3.11 rules them all"

BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
))

server = smtplib.SMTP(HOST)
server.sendmail(FROM, [TO], BODY)
server.quit()