class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = []
        maxi = 0

        for point in points:
            ans.append(point[0])

        ans.sort()

        for i in range(len(ans)):
            maxi = max(maxi, ans[i] - ans[i-1])

        return maxi
