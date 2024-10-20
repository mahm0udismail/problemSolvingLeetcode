class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d=dict()
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return [k for k,v in d.items() if v==2]
        