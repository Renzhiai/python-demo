# coding = utf-8
# !/usr/bin/python
import os


# 删除类型为txt的文件
match_type = '.txt'
# 哪个目录下的文件需要删除
dir_path = "D:/test/"

for filename in os.listdir(dir_path):
    if filename.endswith(match_type):
        file_path = os.path.join(dir_path, filename)
        os.remove(file_path)
        print(f'{file_path}：删除成功')
