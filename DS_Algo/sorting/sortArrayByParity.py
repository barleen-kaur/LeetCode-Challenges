'''
905. Sort Array By Parity: Easy

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        i,j = 0, len(A) - 1
        
        while i < j:
            
            if A[i] % 2 == 0:
                i += 1
                
            elif A[j] %2 != 0:
                j -= 1
                
            else:
                A[i], A[j] = A[j], A[i]
        
        return A