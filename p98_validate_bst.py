# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float("-inf"), float("inf"))
        
    def valid(self, node, left, right):
        if node == None:
            return True
        if (node.val >= right) or (node.val <= left):
            return False
        return (self.valid(node.left, left, node.val) and self.valid(node.right, node.val, right))
