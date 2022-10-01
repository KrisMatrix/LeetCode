"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.store = []
        self.for_node(root)
        return self.store
    
    def for_node(self, node):
        if node == None:
            return
        self.store.append(node.val)
        if len(node.children) != 0:
            for i in range(len(node.children)):
                self.for_node(node.children[i])
