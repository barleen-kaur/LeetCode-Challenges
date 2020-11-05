''' 
Q. Sum of Root To Leaf Binary Numbers
You are given the root of a binary tree where each node has a value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers. The answer is guaranteed to fit in a 32-bits integer.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def returnSum(self, root, sum_):
        if root == None:
            return 0
        if not root.left and not root.right:
            return 2*sum_ + root.val
        else:
            sum_ = 2*sum_ + root.val
            return self.returnSum(root.left, sum_) + self.returnSum(root.right, sum_)
        
            
            
            
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        return self.returnSum(root, 0)