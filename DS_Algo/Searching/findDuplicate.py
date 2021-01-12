'''
287. Find the Duplicate Number: Medium
Q. Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        '''
        #Solution 1
        visited = set()
        for ele in nums:
            if ele in visited:
                return ele
            visited.add(ele)
        '''
        
        #Solution 2 : Detect a cycle
        
        slow = fast = nums[0]
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
    
        fast = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow