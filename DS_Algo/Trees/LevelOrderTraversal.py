'''
Q. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

Output:
[
  [3],
  [9,20],
  [15,7]
]
'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]: 
        '''
        #Recursive
        global sol
        sol = {}
        def returnLevelOrder(root, level):
            global sol
            if root == None:
                return
            else:
                if level not in sol:
                    sol[level] = [root.val]
                else:
                    sol[level] += [root.val]
                returnLevelOrder(root.left, level+1)
                returnLevelOrder(root.right, level+1)
        
        returnLevelOrder(root, 0)
        return sol.values()
        '''
        #Iterative using Queues
        Queue = []
        LOT = []
        if root == None: 
            return []
        else:
            Queue.append([root, 0])
            
        while len(Queue) > 0:
            
            curr, level = Queue.pop(0)
            if len(LOT) > level:
                LOT[level] += [curr.val]
            else:
                LOT.append([curr.val]) 

            if curr.left:
                Queue.append([curr.left, level+1])
                
            if curr.right:
                Queue.append([curr.right, level+1])
                
        return LOT