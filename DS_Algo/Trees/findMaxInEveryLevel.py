'''
Q. Find Largest Value in Each Tree Row
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        global sol
        sol = []
        def LevelOrder(root, lvl):
            global sol
            if root == None:
                return 
            if len(sol) <= lvl:
                sol.append(-float('inf'))
   
            sol[lvl] = max(sol[lvl], root.val)
            LevelOrder(root.left, lvl+1)
            LevelOrder(root.right, lvl+1)
                
        LevelOrder(root, 0)
        return sol