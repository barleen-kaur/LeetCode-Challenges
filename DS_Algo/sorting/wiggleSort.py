'''
280. Wiggle Sort : Medium
Q. Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
'''

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()    
        i = 1
        n = len(nums)-1
        j = n if n%2 == 0 else n-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 2
            j -= 2