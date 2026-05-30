# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        diameter = float('-inf')
        def dfs(node):
            nonlocal diameter
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter,max(left,0)+max(right,0)+node.val,node.val)
            return node.val+max(left,right,0)
        dfs(root)
        return diameter
            
        