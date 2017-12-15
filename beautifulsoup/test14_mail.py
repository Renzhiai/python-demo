# coding:utf-8
import warnings
warnings.filterwarnings('ignore')

import smtplib
from email.mime.text import MIMEText

msg=MIMEText('The body of the email is here')
msg['Subject'] = "An Email Alert"
msg['From'] = "rza1314@163.com"
msg['To'] = "testrenzhiai@163.com"

mail_host='smtp.163.com'

s=smtplib.SMTP()
s.connect(mail_host)
s.login('rza1314@163.com','password')
s.send_message(msg)
s.quit()
