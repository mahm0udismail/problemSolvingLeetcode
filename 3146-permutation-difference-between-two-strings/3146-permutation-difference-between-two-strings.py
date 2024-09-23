class Solution(object):
    def findPermutationDifference(self, s, t):
        diff = 0
        for i in range(len(s)):
            diff += abs(s.index(s[i]) - t.index(s[i]))
        return diff
        