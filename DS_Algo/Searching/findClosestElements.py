'''
658. Find K Closest Elements: Medium
Q. Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[-k:]
        
        def binarySearch(num):
            
            low, high = 0, len(arr)-1
            
            while low < high:

                mid = low + (high-low)//2
                curr = arr[mid]
                if curr == num:
                    return mid
                elif curr > num:
                    high = mid
                else:
                    low = mid+1
                    
            return low
        
    
        idx = binarySearch(x)
        
        low, high = max(0, idx-k-1), min(idx+k-1, len(arr)-1)
        while high-low > k-1:
            if low < 0 or abs(arr[low]-x) <= abs(arr[high]-x):
                high -= 1
            elif high > len(arr) -1  or abs(arr[low]-x) > abs(arr[high]-x):
                low += 1  
        return arr[low:high+1]