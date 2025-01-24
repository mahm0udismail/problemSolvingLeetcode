class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(height)):
            if i > 0 and height[i-1] > threshold:
                ans.append(i)
        return ans