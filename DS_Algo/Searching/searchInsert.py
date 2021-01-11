'''
35. Search Insert Position: Easy
Q. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        low, high = 0, len(nums)-1
        
        while low < high:
            
            mid = low + (high-low)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        
        return low if nums[low] >= target else low + 1