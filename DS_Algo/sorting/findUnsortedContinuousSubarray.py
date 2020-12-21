'''
581. Shortest Unsorted Continuous Subarray: Medium
Q. Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
'''
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        '''
        #Solution 1 : Sort and compare
        sortnums = sorted(nums)
        
        minidx = - 1
        maxidx = - 1
        for idx, (a, b) in enumerate(zip(nums, sortnums)):
            if a != b:
                if minidx == -1:
                    minidx = idx
                maxidx = max(maxidx, idx)
        
        if minidx >= 0:
            return (maxidx - minidx + 1)
        else:
            return 0
    
         '''       
        #Solution 2 :  check slope
        
        minidx = float('inf')
        maxidx = -float('inf')
        
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                minidx = min(minidx, stack.pop())
            stack.append(i)
                
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                maxidx = max(maxidx, stack.pop())
            stack.append(i)
            
        if minidx < float('inf'):
            return (maxidx - minidx + 1) 
        
        else:
            return 0


