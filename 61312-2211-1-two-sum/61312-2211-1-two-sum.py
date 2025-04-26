class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i,n in enumerate(nums):
            n2 = target - n 
            if n2 in hashmap:
                return [hashmap[n2], i]
            hashmap[n]=i