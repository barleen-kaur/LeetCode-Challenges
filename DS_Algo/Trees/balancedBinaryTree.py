'''
Q.  Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: TreeNode) -> bool:
        global res 
        res = True
        def checkBalance(root):
            global res
            if root == None:
                return 0
            elif not root.left and not root.right:
                return 0
            else:
                left =  int(root.left != None) + checkBalance(root.left)
                right = int(root.right != None) + checkBalance(root.right)
                res = res and abs(left-right) <= 1
                return max(left, right)        
                
        checkBalance(root)
        return res