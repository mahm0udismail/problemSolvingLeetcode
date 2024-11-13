class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # l1 = nums[:n]
        # l2 = nums[n:]
        # new = []
        # for i in range(n):
        #     new.append(l1[i])
        #     new.append(l2[i])
        
        # return new

        new=[]
        for i in range(len(nums)/2):
            new.append(nums[i])
            new.append(nums[n+i])
        return new