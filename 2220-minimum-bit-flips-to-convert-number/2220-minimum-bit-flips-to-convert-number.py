class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """

        """
        count = 0
        startb = bin(start)[2:]
        goalb = bin(goal)[2:]
        max_length = max(len(startb), len(goalb))
        startb = startb.zfill(max_length)
        goalb = goalb.zfill(max_length)
        for i in range(len(startb)):
            if startb[i] != goalb[i]:
                count += 1
        return count
        """
        
        return bin(start ^ goal).count('1')
