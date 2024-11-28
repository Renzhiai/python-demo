# coding=utf-8

import os
import shutil

jmx_path = 'C:\\Users\\admin\\Desktop\\jt\\11-11.jmx'
jtl_path = 'C:\\Users\\admin\\Desktop\\jtest\\test.jtl'
report_path = 'C:\\Users\\admin\\Desktop\\jtest'

# 删除旧的测试数据
if os.path.exists(report_path):
    for item in os.listdir(report_path):
        cur_path = os.path.join(report_path, item)
        if os.path.isdir(cur_path):
            shutil.rmtree(cur_path)
        else:
            os.remove(cur_path)

# 将cmd的显示字符编码从默认的GBK改为UTF-8
os.system('chcp 65001')
cmd = f'jmeter -n -t {jmx_path} -l {jtl_path} -e -o {report_path}'
print(cmd)
result = os.popen(cmd)
print(result.read())
