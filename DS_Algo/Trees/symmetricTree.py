'''
Q: Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        Q = []
        
        if root:
            Q.append((root.left, root.right))
        else:
            return True
        
        while len(Q) > 0:
            
            leftcurr, rightcurr = Q.pop(0)

            if leftcurr == None and rightcurr == None:
                continue
            elif (leftcurr == None or rightcurr == None) or leftcurr.val != rightcurr.val:
                return False
            
            
            Q.append((leftcurr.left, rightcurr.right))
            Q.append((leftcurr.right, rightcurr.left))
            
            
                
        return True