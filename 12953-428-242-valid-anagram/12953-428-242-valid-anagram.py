class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sMap = defaultdict(int)
        tMap = defaultdict(int)
        for i in s:
            sMap[i]+=1
        for i in t:
            tMap[i]+=1
        return sMap == tMap