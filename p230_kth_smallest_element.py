# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sorted_list = []
        self.inorder(root)
        return self.sorted_list.pop(k-1)
        
    def inorder(self,node):
        if node != None:
            self.inorder(node.left)
            self.sorted_list.append(node.val)
            self.inorder(node.right)
