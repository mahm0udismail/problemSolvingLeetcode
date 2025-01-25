class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def backtrack(current):

            if len(current) == n:
                result.append(current)
                return
            
            if not current or current[-1] == '1':
                backtrack(current + '0')
                backtrack(current + '1')
            
            elif current[-1] == '0':
                backtrack(current + '1')
    
        result = []
        backtrack("")
        return result