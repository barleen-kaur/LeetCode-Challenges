'''
179. Largest Number: Medium
Q. Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

'''

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(x,y):
            if x+y > y+x:
                return -1
            elif x+y == y+x:
                return 0
            else:
                return 1
        
        for i, num in enumerate(nums):
            nums[i] = str(nums[i])

        nums.sort(key = cmp_to_key(compare))
        return ''.join(nums) if nums[0] != '0' else '0'