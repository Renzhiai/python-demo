# coding:utf-8
class Solution(object):
    def twoSum(self,nums,target):
        """
        给定一个数组和一个目标值，数组里面其中两个元素的和为这个目标值
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    print [i, j]

nums=[1,4,5,7]
target=11
s=Solution()
s.twoSum(nums,target)
