'''
162. Find Peak Element: Medium
Q. A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def binarySearch(low, high):
            
            if low == high:
                return low
            
            mid = low + (high-low)//2
            
            if nums[mid] > nums[mid+1]:
                return binarySearch(low, mid)
            else:
                return binarySearch(mid+1, high)
                
                
        return binarySearch(0, len(nums)-1)