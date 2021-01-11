'''
718. Maximum Length of Repeated Subarray: Medium
Q. Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
'''

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        
        res = -float('inf')
        tab = [[0]*(len(A)+1) for i in range(len(B)+1)]
        for j in range(len(B)):
            for i in range(len(A)):
                if A[i] == B[j]:
                    tab[j][i] = tab[j-1][i-1]+1
            res = max(max(tab[j]),res)         
        return res