# coding: utf-8
import random
import string


def get_verification_code(length=4):
    letters = string.ascii_letters + string.digits
    code = ''
    for _ in range(length):
        # 重复
        code += random.choice(letters)
        # 不重复
        # code += random.sample(letters)
    return code


verification_code = get_verification_code()
print(verification_code)
