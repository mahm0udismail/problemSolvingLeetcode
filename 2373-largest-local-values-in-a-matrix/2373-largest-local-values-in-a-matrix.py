class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        maxLocal = [[0]*(n-2) for i in range(n-2)]

        for i in range(1,n-1):
            for j in range(1,n-1):
                maxLocal[i-1][j-1] = max(maxLocal[i-1][j-1],grid[i-1][j],grid[i-1][j-1],grid[i-1][j+1],grid[i+1][j],grid[i+1][j+1],grid[i+1][j-1],grid[i][j-1],grid[i][j],grid[i][j+1])

        return maxLocal