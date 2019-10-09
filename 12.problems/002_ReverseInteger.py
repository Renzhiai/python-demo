# coding:utf-8
class Solution(object):
    def reverse(self, x):
        """
        反转一个int数字，比如123输出321,-123输出-321，不能溢出
        :type x: int
        :rtype: int
        """
        rx = ""
        if x >= -2**31 and x <= 2**31-1:
            if x > 0 :
                for i in reversed(str(x)):
                    rx = rx + i
                if int(rx) >= 2**31:
                    rx = 0
                print (int(rx))
                return int(rx)
            else:
                for i in reversed(str(abs(x))):
                    rx = rx + i
                print('b'+rx)
                if int(rx) >= 2**31:
                    rx = 0
                print(int('-'+str(int(rx))))
                return (int('-'+str(int(rx))))
        else:
            print(0)
            return 0

x = 123
s = Solution()
s.reverse(x)