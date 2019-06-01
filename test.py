#!/usr/bin/env
# coding = utf-8
import os
import unittest

cash_path = os.path.join(os.getcwd(),'../test_case')

print('文件地址：', os.getcwd())
print("cash_path:", cash_path)

# discover = unittest.defaultTestLoader.discover(cash_path,
#                                                pattern="test*.py",
#                                                top_level_dir=None)
# top_level_dir : 这个是顶层目录的名称，一般默认等于None就行了

# if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    # runner.run(discover)