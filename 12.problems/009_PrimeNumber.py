# coding:utf-8
from math import sqrt

class Solution():
    def primeNumber(self,n):
        """
        求n以内的素数
        :type x: int
        :rtype: list
        """
        rList = []
        for i in range(2, n):
            flag = 1
            for j in range(2, int(sqrt(n)) + 1):
                if i % j == 0 and i != j:
                    flag = 0
                    break
            if flag == 1:
                rList.append(i)
        print(rList)
    
s = Solution()
s.primeNumber(169)