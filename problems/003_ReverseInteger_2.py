# coding:utf-8
import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # sys.maxint
        if x > -2**31 and x < 2**31:
            s = cmp(x, 0)
            r = int(str(x * s)[::-1])
            if r > -2**31 and r < 2**31:
                print('aaa')
                return s * r * (r < 2**31)
            else:
                print(0)
                return 0
        else:
            print(1)
            return 0

x = 1534236469
s = Solution()
s.reverse(x)