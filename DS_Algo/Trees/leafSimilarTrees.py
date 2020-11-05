'''
Q. Leaf-Similar Trees
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence. 
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def checkLeaf(root, lst):
            if root == None:
                return
            if not root.left and not root.right:
                lst.append(root.val)
            else:
                checkLeaf(root.left, lst)
                checkLeaf(root.right, lst)
                
            return lst
        
        lst1 = checkLeaf(root1, [])
        lst2 = checkLeaf(root2, [])
    
        return lst1 == lst2