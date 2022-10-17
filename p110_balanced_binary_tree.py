# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        status, height = self.return_data(root) 
        return status

    def return_data(self, node):
        if node.left == None and node.right == None:
            return True, 1
        if node.left != None:
            left_b, left_s = self.return_data(node.left)
            left_s += 1
        else:
            left_b, left_s = True, 1
        if node.right != None:
            right_b, right_s = self.return_data(node.right)
            right_s += 1
        else:
            right_b, right_s = True, 1
            
        if abs(left_s - right_s) > 1:
            return False, max(left_s, right_s)
        if left_b and right_b:
            return True, max(left_s,right_s)
        else:
            return False,max(left_s,right_s)
