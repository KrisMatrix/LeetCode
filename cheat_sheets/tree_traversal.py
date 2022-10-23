def preorder(root: TreeNode) -> None:
    if not root: return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def inorder(root: TreeNode) -> None:
    if not root: return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def postorder(root: TreeNode) -> None:
    if not root: return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

# Consider the tree:
#
#                       7 
#                   /       \
#               1               9
#           /       \       /       \
#          0         3    8         10
#                  /  \
#                2     5
#                     / \
#                   4    6
#
#
#Pre-order traversal:
#
#Summary: Begins at the root (7), ends at the right-most node (10)
#
#Traversal sequence: 7, 1, 0, 3, 2, 5, 4, 6, 9, 8, 10
#
#In-order traversal:
#
#Summary: Begins at the left-most node (0), ends at the rightmost node (10)
#
#Traversal Sequence: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#
#Post-order traversal:
#
#Summary: Begins with the left-most node (0), ends with the root (7)
#
#Traversal sequence: 0, 2, 4, 6, 5, 3, 1, 8, 10, 9, 7

# When to use Pre-Order, In-order or Post-Order?
# The traversal strategy the programmer selects depends on the specific 
# needs of the algorithm being designed. The goal is speed, so pick the 
# strategy that brings you the nodes you require the fastest.
#
# If you know you need to explore the roots before inspecting any leaves, 
# you pick pre-order because you will encounter all the roots before all 
# of the leaves.
#
# If you know you need to explore all the leaves before any nodes, you 
# select post-order because you don't waste any time inspecting roots 
# in search for leaves.
#
# If you know that the tree has an inherent sequence in the nodes, and 
# you want to flatten the tree back into its original sequence, than an 
# in-order traversal should be used. The tree would be flattened in the 
# same way it was created. A pre-order or post-order traversal might not 
# unwind the tree back into the sequence which was used to create it.


def levelorder(root: TreeNode) -> None:
    if not root: return
    q = deque([root])
    
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            print(str(node.val), end = " ")
            if node.left: 
                q.append(node.left)
            if node.right: 
                q.append(node.right)

        print()
