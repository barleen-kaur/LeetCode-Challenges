'''
1337. The K Weakest Rows in a Matrix: Easy
Q. Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.

 

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]
'''


class Solution:
    def binarySearch(self, mat, row):
        
        low, high = 0, len(mat[row])
        
        while low < high:
            
            mid  = low + (high-low)//2
            curr = mat[row][mid]
            
            if curr == 0:
                high = mid
                
            else:
                low = mid + 1
                
        return low
                
        
        
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        sumMat = collections.Counter()
        row, col = len(mat), len(mat[0])
        
        for i in range(row):
            sumMat[i] = self.binarySearch(mat, i)
        
        sortedsum = sorted(sumMat.items(), key = lambda x:x[1])

        
        return [kv[0] for i,kv in enumerate(sortedsum) if i<k]