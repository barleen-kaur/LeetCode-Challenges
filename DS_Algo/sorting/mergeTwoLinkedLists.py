'''
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Input: l1 = [], l2 = []
Output: []
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        if l1.val > l2.val:
            start = head =  l2
            l2 = l2.next
        
        else:
            start = head = l1
            l1 = l1.next
        print(head.val)   
        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
            print(head.val)
                
        if l1:
            head.next = l1
        

        if l2:
            head.next = l2
            
            
        return start