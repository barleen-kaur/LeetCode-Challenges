'''
Q. Cousins in Binary Tree
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Input: root = [1,2,3,4], x = 4, y = 3
Output: false
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        queue = []
        if root == None:
            return False
        else:
            ans = []
            queue.append([root, 0])
            if root.val == x or root.val == y:
                ans.append([0, None])
            
        while queue:
            
            curr, depth = queue.pop(0)
            
            if curr.left:
                queue.append([curr.left, depth+1])
                if curr.left.val == x or curr.left.val == y:
                    ans.append([depth+1, curr.val])
            if curr.right:
                queue.append([curr.right, depth+1])
                if curr.right.val == x or curr.right.val == y:
                    ans.append([depth+1, curr.val])
                    
        return ans[0][0] == ans[1][0] and ans[0][1] != ans[1][1]