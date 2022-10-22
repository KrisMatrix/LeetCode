# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_val = 0
        self.return_height_and_daimeter(root)
        return self.max_val
    
    def return_height_and_daimeter(self,node):
        if not node:
            return -1
        l = self.return_height_and_daimeter(node.left)
        r = self.return_height_and_daimeter(node.right)
            
        self.max_val = max(self.max_val, l + r + 2)
        return 1 + max(l,r) #return the height
    
# For each node, calculate the diameter and height. 
# update a max_val if the value is less than diameter
# function must return height
# height = 1 + max(l,r)
# diameter = l + r + 2
