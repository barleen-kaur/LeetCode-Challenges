'''
Q: Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''
        #Recursive
        if p == None and q == None:
            return True
        elif (p == None or q == None) or p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        '''
        
        #Iterative
        Q = []
        if p and q:
            if p.val != q.val:
                return False
            
            Q.append((p.left, q.left))
            Q.append((p.right, q.right))
            
        else:
            return p == q

        while len(Q) > 0:
            
            t1, t2 = Q.pop(0)
            
            if t1 == None and t2 == None:
                continue
            elif (t1 == None or t2 == None) or t1.val != t2.val:
                return False
            
            Q.append((t1.left, t2.left))
            Q.append((t1.right, t2.right))
            
        
        return True