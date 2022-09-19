import os
import re

filename = re.compile('.*(.gif)$')

dir_path = "D:/test/"
os.chdir("d:/test")
for file in os.listdir(dir_path):
    if os.path.exists(file):
        if filename.match(file):
            os.remove(file)
            print(file)
