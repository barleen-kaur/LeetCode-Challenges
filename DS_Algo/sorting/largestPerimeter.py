'''
976. Largest Perimeter Triangle: Easy
Q. Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
'''


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        
        if len(A) < 3:
            return 0
        
        A.sort()
        i = len(A)-1
        while i-2 >= 0:
            s1, s2, s3 = A[i-2], A[i-1], A[i]
            
            if s1 + s2 > s3:
                return s1+s2+s3
            else:
                i -= 1
                
        return 0
            