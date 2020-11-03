'''
Q. Convert Sorted Array to Binary Search Tree:

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def returnBST(self, root, nums, l, h, left):
        
        if l <= h:
            mid = l + (h-l)//2
            if left:
                root.left = TreeNode(val=nums[mid])
                self.returnBST(root.left, nums, l, mid-1, 1)
                self.returnBST(root.left, nums, mid+1, h, 0)
            else:
                root.right = TreeNode(val=nums[mid])
                self.returnBST(root.right, nums, l, mid-1, 1)
                self.returnBST(root.right, nums, mid+1, h, 0)
            
        
        
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        n = len(nums)
        l = 0
        h = n - 1
        
        if n > 0:
            mid = l + (h-l)//2
            start = TreeNode(val=nums[mid])
            self.returnBST(start, nums, l, mid-1, 1)
            self.returnBST(start, nums, mid+1, h, 0)
        
        else:
            return None
        
        return start