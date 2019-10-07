#!/usr/bin/env
# coding = utf-8
import unittest

# 编写单元测试时，我们需要编写一个测试类，从 unittest.TestCase 继承
class MyTest(unittest.TestCase):
    def setUp(self):
        # 每个测试用例执行之前做操作
        print('start')

    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('end')

    # 测试用例a，方法名必须test开头
    def test_a(self):
        self.assertEqual(1, 1)

    # 测试用例b
    def test_b(self):
        self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()