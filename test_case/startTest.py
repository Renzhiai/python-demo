# coding:utf-8
import time

class OneAreaLaunchSpeedTest(object):
    '''
    测试1号社区启动速度
    '''
    def test(self):
        #测试100轮冷启动与热启动
        for i in range(0,100):
            self.device.start_app()
            self.device.clear_app()
            time.sleep(5)