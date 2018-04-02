# coding:utf-8
class Solution(object):
    def bubbleSort(self, li):
        """
        冒泡排序
        :type x: list
        :rtype: list
        """
        for i in range(len(li)):
            for j in range(i, len(li)):
                print(i, j)
                if li[i] > li[j]:
                    li[i], li[j] = li[j], li[i]
        print(li)

