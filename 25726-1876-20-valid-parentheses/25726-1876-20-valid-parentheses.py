class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        match = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = [s[0]]
        for char in s[1:]:
            if char in match.keys() and len(stack) == 0:
                return False
            elif char in match.keys() and match[char] != stack[-1]:
                return False
            elif char in match.keys():
                stack.pop(-1)
            elif char not in match.keys():
                stack.append(char)
        return len(stack) == 0
