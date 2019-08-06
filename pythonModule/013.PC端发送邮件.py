#coding:utf-8
from email.mime.text import MIMEText
import smtplib

sender='rza0925@163.com'
receiver='testrenzhiai@163.com'
#邮件主题
subject='python测试邮件'
#发送邮箱服务器
smtpserver='smtp.163.com'
#发送方帐号密码
username=sender
password='*********'
	
msg=MIMEText('你好！','plain','utf-8')
msg['From']=sender
msg['To']=receiver
msg['Subject']=subject

server=smtplib.SMTP()
server.connect(smtpserver,'25')
#server.set_debuglevel(1)
server.login(username,password)
server.sendmail(sender,receiver,str(msg))
server.quit()
