'''
Q. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        '''
        
        #Iterative
        queue = []
        if root == None:
            return 0
        else:
            queue.append([root, 0])
            arr = []
            
        while queue:
            
            curr, depth = queue.pop(0)
        
            if len(arr) <= depth:
                arr.append(curr.val)
            
            else:
                arr[-1] += curr.val
                
            if curr.left:
                queue.append([curr.left, depth+1])

            if curr.right:
                queue.append([curr.right, depth+1])
                          
        return arr.index(max(arr)) + 1
        '''
        
        # Recursive
        global sol
        sol = []
        def dfs(root, depth):
            if root == None:
                return 
            else:
                if len(sol) <= depth:
                    sol.append(root.val)
                else:
                    sol[depth] += root.val
                dfs(root.left, depth+1)
                dfs(root.right, depth+1)
        
        dfs(root,0)
        print(sol)
        return sol.index(max(sol)) + 1