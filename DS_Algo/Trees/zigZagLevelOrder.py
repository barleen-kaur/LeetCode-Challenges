'''
Q. Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
Output: [
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        #Recursive
        global sol
        sol = {}
        def returnzigzag(root, level, flag):
            global sol
            if root == None:
                return
            else:  
                if flag:
                    if level not in sol:
                        sol[level] = [root.val]
                    else:
                        sol[level] = [root.val] + sol[level]
                        
                else:
                    if level not in sol:
                        sol[level] = [root.val]
                    else:
                        sol[level] += [root.val]
                        
                returnzigzag(root.right, level+1, not flag)
                returnzigzag(root.left, level+1, not flag)
                            
        returnzigzag(root, 0 , True)
      
        return sol.values()
    
        '''
        #Iterative
        sol = []
        queue = []
        if root == None:
            return []
        else:
            queue.append([root,0])

        while queue:
        
            curr, lvl = queue.pop(0)
            if len(sol) <= lvl:
                sol.append([curr.val])
            else:
                if lvl % 2 == 0:
                    sol[lvl] += [curr.val]
                else:
                    sol[lvl] = [curr.val] + sol[lvl]
                    
            if curr.left:
                queue.append([curr.left, lvl+1])
            if curr.right:
                queue.append([curr.right, lvl+1])
            
        return sol  