# coding:utf-8
class Solution(object):
    def duplicate(self, li):
        """
        对一个list去重
        :type x: list
        :rtype: list
        """
        listNew = []
        for i in li:
            if i not in listNew:
                listNew.append(i)
        print(listNew)

li = [2, 4, 6, 2, 6, 5]
s = Solution()
s.duplicate(li)
