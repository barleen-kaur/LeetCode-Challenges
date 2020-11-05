'''
Q. Increasing Order Search Tree
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

Output: BST skewed right
[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    start = None
    prev = None
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def traverseCreate(root):
            if root == None:
                return None
            else:
                traverseCreate(root.left)  
                newroot = TreeNode(root.val)
                if self.prev == None:
                    self.start = newroot
                else:
                    self.prev.right = newroot
                self.prev = newroot
                traverseCreate(root.right)
                
        traverseCreate(root)
        return self.start
        