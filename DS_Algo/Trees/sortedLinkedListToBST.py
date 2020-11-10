'''
Q. Convert Sorted List to Binary Search Tree
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def returnBST(self, root, start, end, left, queue):
        tmp = mid = start
        if start != None and end != None and (start != end or start.val not in queue) :
            if tmp.next and tmp.next.next:
                while tmp.next != end.next and tmp.next.next != end.next:
                    tmp = tmp.next.next
                    mid = mid.next

        else:
            return 
                
        if left:
            root.left = TreeNode(val = mid.val)
            queue.append(mid.val)
            self.returnBST(root.left, start, mid, 1, queue)
            self.returnBST(root.left, mid.next, end, 0, queue)
        
        else:
            root.right = TreeNode(val = mid.val)
            queue.append(mid.val)
            self.returnBST(root.right, start, mid, 1, queue)
            self.returnBST(root.right, mid.next, end, 0, queue)
    
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        start = mid = head
        
        if start == None:
            return None
        
        while start.next and start.next.next:
            start = start.next.next
            mid = mid.next
        
        left = head
        right = start if start.next == None else start.next
        queue = []
        
        root = TreeNode(val=mid.val)
        queue.append(mid.val)
        self.returnBST(root, left, mid, 1, queue)
        self.returnBST(root, mid.next, right, 0, queue)
          
        return root
            

