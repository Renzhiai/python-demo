#coding: utf-8
import random
letters="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
code=""
#code=[]
for i in range(4):
	code+=random.choice(letters)
	#code.append(random.choice(letters))
print(code)
