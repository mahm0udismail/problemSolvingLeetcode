class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        if nums==[]:
            return []
        for i in range(k):
            m=nums[0]
            ind=0
            for j in range(len(nums)):
                if nums[j]<m:
                    m=nums[j]
                    ind=j
            nums[ind]=nums[ind]*multiplier
        return nums