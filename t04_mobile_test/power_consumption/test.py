# coding=utf-8
import subprocess
import threading
import time


def get_packages():
    '''
    获取所有的包名
    :return:
    '''
    # 保存所有的包
    all_packages = []
    # 存储包名
    packages = []
    # 获取所有的包
    cmd = 'adb shell pm list package'
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # 以换行来划分
    output = proc.communicate()[0].split('\n')
    print(output)
    for package in output:
        #     去掉package:字符串
        if 'package:' in package:
            # 去掉\r
            package = package[8:].replace('\r', '')
            packages.append(package)
            if len(packages) == 10:
                all_packages.append(packages)
                packages = []
            elif package in output[len(output) - 2]:
                all_packages.append(packages)
    print(output[len(output) - 2])
    print(all_packages)
    return all_packages


get_packages()
