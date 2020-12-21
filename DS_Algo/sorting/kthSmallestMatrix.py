'''
378. Kth Smallest Element in a Sorted Matrix: Medium
Q. Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        
        heap = []
        
        for ro in range(min(rows, k)):
            heap.append((matrix[ro][0], ro, 0))
            
        
        heapq.heapify(heap)
        
        while k > 0:
            
            ele, r, c = heapq.heappop(heap)
            
            if c < cols-1:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))
            
            k -= 1
            
        return ele