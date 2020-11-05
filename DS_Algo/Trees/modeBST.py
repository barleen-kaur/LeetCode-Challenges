'''
Q. Find Mode in Binary Search Tree
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
       
        global modes 
        modes = {}
        
        def returnModes(root):
            global modes
            
            if root == None:
                return root
            else:
                if root.val not in modes:
                    modes[root.val] = 1
                else:
                    modes[root.val] += 1
                
                returnModes(root.left)
                returnModes(root.right)
                
        returnModes(root)
        sol = []
        if root == None:
            return sol
        
        max_mode = max(modes.values())
        for key, val in modes.items():
            if val == max_mode:
                sol.append(key)
                
        return sol