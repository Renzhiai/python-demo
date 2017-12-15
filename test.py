# coding:utf-8
import mock
import unittest

from test2 import Count

# test Count class
class TestCount(unittest.TestCase):

    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=13,side_effect=count.add)
        result = count.add(7,7)
        print(result)
        count.add.assert_called_with(7,7)
        self.assertEqual(result,13)

if __name__ == '__main__':
    unittest.main()