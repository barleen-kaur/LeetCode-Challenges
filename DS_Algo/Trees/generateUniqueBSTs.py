'''
Q. Unique Binary Search Trees II
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def returnBSTs(low, high):
            if low > high:
                return [None]
            
            sol = []
            
            for i in range(low, high+1):
                leftchildren = returnBSTs(low, i-1)
                rightchildren = returnBSTs(i+1, high)
                for left in leftchildren:
                    for right in rightchildren:
                        root = TreeNode(val=i)
                        root.left = left
                        root.right = right
                        sol.append(root)
            return sol
        
        return returnBSTs(1,n) if n > 0 else []