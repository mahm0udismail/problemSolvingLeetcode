class Solution(object):
    @staticmethod
    def sub(x,z):
        return abs(int(x) - int(z))
    def scoreOfString(self, s):
        sum = 0
        for i in range(len(s) - 1):
            sum += self.sub(ord(s[i]), ord(s[i + 1]))
        return sum

# class Solution(object):
#     def scoreOfString(self, s):
#         sum=0
#         for i in range(1, len(s)):
#             sum+=abs(ord(s[i])-ord(s[i-1]))
#         return sum
        