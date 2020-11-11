'''
Q. Check Completeness of a Binary Tree
Given a binary tree, determine if it is a complete binary tree.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    numNodes = 0
    maxIdx = 0
    def isCompleteTree(self, root: TreeNode) -> bool:
        
        # Recursive
        '''
        
        def dfs(root, index):
            if root:
                self.numNodes += 1
                self.maxIdx = max(index, self.maxIdx)
                dfs(root.left, 2*index)
                dfs(root.right, 2*index + 1)
                
        dfs(root, 1)
        return self.numNodes == self.maxIdx
        '''
    
        #Iterative
        if root == None:
            return True
        else:
            queue = [root]
            
        while queue[0] != None:
            curr = queue.pop(0)
            
            queue.append(curr.left)
            queue.append(curr.right)
            
        
        while len(queue) > 0 and queue[0] == None:
            queue.pop(0)
            
        return len(queue) == 0