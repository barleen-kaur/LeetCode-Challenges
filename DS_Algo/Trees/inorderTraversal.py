'''
Q. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Recursive solution is trivial, could you do it iteratively also?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        #Recursive
        sol = []
        def traverse(root, sol):
            if root == None:
                return 
            else:
                traverse(root.left, sol)
                sol.append(root.val)
                traverse(root.right, sol)
            return sol
        return traverse(root, sol)
        '''
        
        #Iterative
        stack = []
        visited = []
        
        while True:
            while root:
                visited.append(root)
                root = root.left
            
            if len(visited) < 1:
                break
                
            root = visited.pop()
            stack.append(root.val)
            root = root.right
            
        return stack