'''
148. Sort List: Medium
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        def MergeSort(head):
            
            if head.next == None:
                return head
            
            st = mid_prev = head
            while head and head.next and head.next.next:
                mid_prev = mid_prev.next
                head = head.next.next
  
            mid = mid_prev.next
            mid_prev.next = None

            while st and mid:
                
                left = MergeSort(st)
                right = MergeSort(mid)

                return Merge(left, right)
                
        
        def Merge(st, mid):
            
            dummy = ListNode(0)
            tmp = dummy
        
            while st != None and mid != None:
                if st.val > mid.val:
                    tmp.next = mid
                    mid = mid.next
                else:
                    tmp.next = st
                    st = st.next
                tmp = tmp.next
                    
            if st != None:
                tmp.next = st
                
            elif mid != None:
                tmp.next = mid
            
            return dummy.next
            
        return MergeSort(head)
                
                 
            
            
                
                
        