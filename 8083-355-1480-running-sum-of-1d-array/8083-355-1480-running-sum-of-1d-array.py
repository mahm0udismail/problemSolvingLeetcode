class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # new=[]
        # for i in range(1,len(nums)+1):
        #     count=0
        #     for j in range(i):
        #         count=count+nums[j]
        #     new.append(count)
        # return new
        sum = 0
        for i in range(len(nums)):
            nums[i] = nums[i] + sum
            sum = nums[i]
        return nums
        