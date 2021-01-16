'''
1064. Fixed Point: Easy
Q. Given an array of distinct integers arr, where arr is sorted in ascending order, return the smallest index i that satisfies arr[i] == i. If there is no such index, return -1.

Example 1:

Input: arr = [-10,-5,0,3,7]
Output: 3
Explanation: For the given array, arr[0] = -10, arr[1] = -5, arr[2] = 0, arr[3] = 3, thus the output is 3.
Example 2:

Input: arr = [0,2,5,8,17]
Output: 0
Explanation: arr[0] = 0, thus the output is 0.

'''


class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        
        low, high = 0, len(arr)-1
        
        while low <= high:
            
            mid = low + (high-low)//2
            curr = arr[mid]
            
            if curr == mid:
                pos = mid
                while pos >= 0 and arr[pos] == pos:
                    pos -= 1
                if pos < mid:
                    return pos+1
                else:
                    return mid
                
            elif curr > mid:
                high = mid - 1
                
            else:
                low = mid + 1
                
        
        return -1