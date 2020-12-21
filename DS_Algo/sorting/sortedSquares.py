'''
977. Squares of a Sorted Array: Easy
Q. Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        '''
        # Solution 1
        return sorted(x*x for x in nums)
        '''
        
    
        #Solution 2
        n = len(nums)
        i = 0
        while i < n and nums[i] < 0:
            i += 1
        
        i, j = i-1 , i
        ans = []
        while i >= 0 and j < n:
            if nums[i]**2 < nums[j]**2:
                ans.append(nums[i]**2)
                i -= 1
            else:
                ans.append(nums[j]**2)
                j += 1
                
        while i >= 0:
            ans.append(nums[i]**2)
            i -= 1
            
        while j < n:
            ans.append(nums[j]**2)
            j += 1
            
        return ans