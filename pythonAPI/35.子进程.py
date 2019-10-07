#coding:utf-8
import subprocess

cmd = 'java -verison'
res = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
print(res.stdout)
a = res.communicate('exit\n')
print(a)