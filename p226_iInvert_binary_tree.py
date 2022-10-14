# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swap_nodes(root)
        return root
    
    
    def swap_nodes(self, node):
        if node == None:
            return
        left = node.left
        node.left = node.right
        node.right = left
        self.swap_nodes(node.left)
        self.swap_nodes(node.right)
