# coding:utf-8
import unittest
import HTMLTestRunner
import sys
import os

if __name__ == '__main__':
    tp = './'
    # fp = os.path.join(sys.argv[1], 'result.html')
    fp = '/root/.jenkins/workspace/report/result.html'
    ts = unittest.defaultTestLoader.discover(tp, pattern='TC*.py')
    # ts = unittest.defaultTestLoader.discover(path, pattern='select*.py')
    f = open(fp, mode='wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='测试报告', description='用例执行情况')
    runner.run(ts)
    f.close()