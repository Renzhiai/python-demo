# coding=utf-8
from email.mime.text import MIMEText
import smtplib
from email.header import Header

# 用户名
uname = ''
# 密码
pwd = ''
# 收件人
toAddr = ''

# msg = MIMEText('回来加班', 'plain', 'utf-8')
msg = MIMEText('<h1 style="color:red">出来上网啊</h1>', 'html', 'utf-8')
msg['From'] = uname
msg['To'] = toAddr
msg['Subject'] = Header('发给xxx的邮件', 'utf8').encode()
smtpServer = 'smtp.163.com'

server = smtplib.SMTP(smtpServer, 25)
# server.set_debuglevel(1)
server.login(uname, pwd)
server.sendmail(uname, [toAddr], msg.as_string())
server.quit()
