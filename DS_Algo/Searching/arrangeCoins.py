'''
441. Arranging Coins: Easy
Q. You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        if n < 1:
            return 0
        '''
        # Solution 1: Recursion : O(n)
        def recursion(n, lvl):
            if n == 0:
                return lvl
            elif n < 0:
                return lvl - 1
            else:
                return recursion(n-lvl-1, lvl+1)
            
            
        return recursion(n,0)
        '''
               
        # Solution 2: Binary Search
       
        low, high = 0, n
        
        while low <= high:
            
            mid = low + (high-low)//2
            curr = mid*(mid+1)//2
            
            if curr == n:
                return mid
            elif curr > n:
                high = mid - 1
            else:
                low = mid + 1
                
        return high