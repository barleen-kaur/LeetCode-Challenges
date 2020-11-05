'''
Q. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree [1,2,3,4,5]

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    
    maxdiam = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(root):
            if root == None:
                return 0
            else:
                l = depth(root.left)
                r = depth(root.right)
                curr = max(l,r, l+r)
                if curr > self.maxdiam:
                    self.maxdiam = curr

            return max(l,r) + 1
        
        depth(root)
        return self.maxdiam