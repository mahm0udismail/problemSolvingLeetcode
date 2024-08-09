# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(arr,start,end):
            if start > end:
                return None
            mid = start + (end - start) // 2
            node = TreeNode(arr[mid])
            node.left = helper(arr,start,mid-1)
            node.right = helper(arr,mid+1,end)
            return node

        n = len(nums)
        if n==0:
            return None
        return helper(nums,0,n-1)
        