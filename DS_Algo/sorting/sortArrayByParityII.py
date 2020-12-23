'''
922. Sort Array By Parity II: Easy
Q. Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.


Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
'''



class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        '''
        #Solution 1
        i = 0
        j = 0
        while i < len(A):
            #print('i: {}, j: {}, A: {}'.format(i, j, A))
            if (i%2 == 0 and A[i]%2 == 0) or (i%2 != 0 and A[i]%2 != 0):
                i += 1
            else:
                if i < len(A)-1:
                    j = i+1
                    if i % 2 == 0:
                        while A[j]%2 != 0:
                            j += 2
                    else:
                        while A[j]%2 == 0:
                            j += 2

                    if j < len(A):
                        A[i], A[j] = A[j], A[i]

        return A
        '''  
        
        #Solution 2
        
        n = len(A) 
        if n < 2:
            return A
        
        i,j = 0, 1
        
        while i < n and j < n:
            
            while i < n and A[i] % 2 == 0:
                i += 2
                
            while j < n and A[j] %2 != 0:
                j += 2
                
            if i < n and j < n:
                 A[i], A[j] = A[j], A[i]
                    
                    
        return A