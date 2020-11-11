'''
Q. Longest ZigZag Path in a Binary Tree

Given a binary tree root, a ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right then move to the right child of the current node otherwise move to the left child.
Change the direction from right to left or right to left.
Repeat the second and third step until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Input: root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
Output: 3
Explanation: Longest ZigZag path in blue nodes (right -> left -> right).


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        global max_val
        max_val = -float('inf')
        def returnZigZagLength(root, par, depth):
            global max_val
            if root == None:
                return 0
            else:
                if depth > max_val:
                    max_val = depth
                    
                if par == None:
                    returnZigZagLength(root.left, root, depth+1)
                    returnZigZagLength(root.right, root, depth+1)
                else:
                    if par.right == root:
                        returnZigZagLength(root.left, root, depth+1)
                        returnZigZagLength(root.right, root, 1)
                    else:
                        returnZigZagLength(root.right, root, depth+1)
                        returnZigZagLength(root.left, root, 1)
                    
            return max_val
    
        if root == None:
            return 0
        returnZigZagLength(root, None, 0)
        return max_val