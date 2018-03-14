# coding:utf-8
from uiautomator import device as d
import time
from datetime import datetime

while True:
    if d(resourceId='com.tcl.eshow:id/iv_qr_code_content').wait.exists():
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+u' 二维码存在')
    else:
        break
    time.sleep(1800)
