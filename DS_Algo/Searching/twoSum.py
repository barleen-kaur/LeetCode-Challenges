'''
167. Two Sum II - Input array is sorted: Easy
Q. Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        # Solution 1: Binary Seach: 0(nlogn)    
        def findBinarySearch(n, idx):
            low, high = 0, len(numbers)-1
            while low < high:
                mid = low + (high-low)//2
                num = numbers[mid]
                if num == n:
                    if idx != mid:
                        return mid
                    else:
                        if low < mid and numbers[mid-1] == n:
                            return mid-1
                        elif high > mid and numbers[mid+1] == n:
                            return mid+1
                            
                elif num > n:
                    high = mid
                else:
                    low = mid+1
            return low if numbers[low] == n else -1
            
        for idx, num in enumerate(numbers):
            rem = target - num
            rem_idx = findBinarySearch(rem, idx)
            if rem_idx != -1:
                return [idx+1, rem_idx+1]
        '''
        
        #Solution 2: Two Pointers: O(n)
        
        low, high = 0, len(numbers)-1
        
        while low < high:
            
            sum_ = numbers[low] + numbers[high]
            
            if sum_ == target:
                return [low+1, high+1]
            
            elif sum_ > target:
                high -= 1
                
            else:
                low += 1