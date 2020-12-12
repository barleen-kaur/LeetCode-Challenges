'''
26. Remove Duplicates from Sorted Array
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.

'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                
        return i + 1

        '''
        #My solution: not perfect, fails on test cases in a stange way: when running on failed twest case separately, it produces correct output!

        i = 0
        while i < len(nums) - 1:            
            if nums[i+1] == nums[i]:
                j = i+1
                while j < len(nums) - 1:
                    nums[j] = nums[j+1]
                    j += 1
                    
                nums = nums[:-1]
            else:
                i += 1
        
        return len(nums)
        '''


