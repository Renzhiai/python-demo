# coding = utf-8
# !/usr/bin/python
import random
import string


def get_rand_code(length=6):
    letters = string.ascii_letters + string.digits
    code = ''
    for _ in range(length):
        # 重复
        code += random.choice(letters)
        # 不重复
        # code += random.sample(letters)
    return code


rand_code = get_rand_code()
print(rand_code)
