'''
1351. Count Negative Numbers in a Sorted Matrix
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

'''

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        '''
        #Solution 1
        rows = len(grid)
        cols = len(grid[0])
        
        i, j  = rows-1, cols-1
        count = 0
        flag = False
        while i >= 0 and j >= 0:
            if grid[i][j] < 0:
                count += 1
                for m in range(j-1, -1, -1):
                    if grid[i][m] < 0:
                        count += 1
                for n in range(i-1, -1, -1):
                    if grid[n][j] < 0 :
                        count += 1
                i -= 1
                j -= 1
            else:
                flag = True
                break
        if not flag:
            if cols < rows:
                for i in range(n, -1, -1):
                    if grid[i][0] < 0:
                        count += 1
        return count
        '''

        #Solution 2
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] < 0:
                    count += cols - j
                    break
       
        return count


        '''
        #Solution 3: Binary Search

        def binarysearch(arr):
            
            low, high = 0, len(arr)-1
            
            while low <= high:
                mid = low + (high-low)//2
                
                if arr[mid] >= 0:
                    low = mid + 1
                    
                else:
                    high = mid - 1
                    
            return low
        
    
        count = 0
        cols = len(grid[0])
        for row in grid:
            idx = binarysearch(row)
            count += cols - idx   
        return count
        '''