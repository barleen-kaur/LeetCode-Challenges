'''
81. Search in Rotated Sorted Array II

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

'''

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
         
        # Solution 1: Worst Case: O(n), best case: O(log n)
        if len(nums) < 1:
            return False

        def binarysearch(arr, target, low, high):
            
            while low <= high:
                mid = low + (high-low)//2
                if arr[mid] == target or arr[low] == target or arr[high] == target:
                    return True
                
                if arr[high] == arr[low]:
                    high -= 1
                    continue

                else:
                    if arr[mid] <= arr[high]:
                        if arr[mid] <= target <= arr[high]:
                            low = mid + 1
                        else:
                            high = mid-1
                    else:
                        if arr[high] <= target <= arr[mid]:
                            high = mid - 1
                        else:
                            low = mid + 1      
            return False
        
        
        return binarysearch(nums, target, 0, len(nums)-1 )
        
        
        
        '''
        # Solution 2 
        if len(nums) < 1:
            return False
        idx = -1
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                idx = i+1
                
        if idx == -1:
            idx = 0
        flag = True if nums[idx] <= target <= nums[-1] else False

        def binarysearch(arr, target, low, high):
            
            while low <= high:
                mid = low + (high-low)//2
                if arr[mid] == target:
                    return True
                else:
                    if arr[mid] < target:
                        return binarysearch(arr, target, mid+1, high)
                    else:
                        return binarysearch(arr, target, low, mid-1)
                    
            return False
        
        
        if flag:
            return binarysearch(nums, target, idx, n-1)
        else:
            return binarysearch(nums, target, 0, idx)

        '''

