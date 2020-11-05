'''
Q. Binary Tree Paths
 
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Input: [1,2,3,null,5]
Output: ["1->2->5", "1->3"]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        global paths 
        paths = []
        
        def findPaths(root, st):
            global paths
            
            if root == None:
                return root
            
            if not root.left and not root.right:
                paths.append(st[:-2])
                
            if root.left:
                findPaths(root.left, st+str(root.left.val)+"->")
            if root.right:
                findPaths(root.right, st+str(root.right.val)+"->")
        
        if root:
            st = str(root.val)+"->"
        else:
            return []
        
        findPaths(root, st)
        return paths