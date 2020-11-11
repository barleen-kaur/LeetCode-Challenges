'''
Q. Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if root == None:
            return []
        global dict_
        dict_ = {}
        def returnDuplicates(root, ans):
            global dict_
            if root == None:
                return "None"
            else:
                entry = str(root.val)+ "," + str(returnDuplicates(root.left, ans)) + "," + str(returnDuplicates(root.right, ans))
                
                if entry not in dict_:
                    dict_[entry] = 1
                else:
                    dict_[entry] += 1
                    if dict_[entry] == 2:
                        ans.append(root)
                return entry
                        
        ans = []
        returnDuplicates(root,ans)
        return ans