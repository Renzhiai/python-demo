# coding:utf-8
class Solution(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    print [i, j]

nums=[1,4,5,7]
target=9
s=Solution()
s.twoSum(nums,target)
