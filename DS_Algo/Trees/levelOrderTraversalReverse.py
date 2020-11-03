'''
Q. Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        '''
        # Iterative
        visited = []
        Q = []
        
        if root:
            visited.append([root.val])
            arr = []
            if root.left:
                arr.append(root.left) 
            if root.right:
                arr.append(root.right)
            if arr != []:
                Q.append(arr)
            
        while len(Q) > 0:
            arr = Q.pop(0)
            visited.append([i.val for i in arr])
            newlevel = []
            while len(arr) > 0:
                curr = arr.pop(0)
                if curr.left:
                    newlevel.append(curr.left) 
                if curr.right:
                    newlevel.append(curr.right) 
            
            if newlevel != []:        
                Q.append(newlevel)
        
        return visited[::-1]
        '''


        #Recursive

        lvt = {}
        def levelorderTraversalReverse(node, depth):
            
            if node == None:
                return
            else:
                if depth not in lvt:
                    lvt[depth] = [node]
                else:
                    lvt[depth] += [node]
                    
                levelorderTraversalReverse(node.left, depth+1)
                levelorderTraversalReverse(node.right, depth+1)
            
        levelorderTraversalReverse(root, 0)
        sol = []
        for key in sorted(lvt.keys(), reverse=True):
            value = [i.val for i in lvt[key]]
            sol.append(value)
        
                
        return sol