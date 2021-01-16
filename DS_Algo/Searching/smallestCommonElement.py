'''
1198. Find Smallest Common Element in All Rows: Medium
Q. Given a matrix mat where every row is sorted in strictly increasing order, return the smallest common element in all rows.

If there is no common element, return -1.


Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5

'''


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        #Solution in Leetcode
        row, col = len(mat), len(mat[0])
        idx = [0]*row
        currmax, cnt = 0, 0
        
        while True:
            for i in range(row):
                while idx[i] < col and mat[i][idx[i]] < currmax:
                    idx[i] += 1
                
                if idx[i] >= col:
                    return -1
                
                if mat[i][idx[i]] != currmax:
                    cnt = 1
                    currmax = mat[i][idx[i]]
                else:
                    cnt += 1
                    if cnt == row:
                        return currmax
        
        
        '''
        #Solution: Using heaps: Time Exceeded Error! :(
        for i in range(row):
            heap.append((mat[i][0], i, 0))
        
        heapq.heapify(heap)
        
        while True:
            
            ele, x, y = heapq.heappop(heap)
            
            arr = []
            while heap:
                val, ro, co = heapq.heappop(heap)
                arr.append([val,ro,co])
                
            if all(v==ele for v,r,c in arr):
                return ele
            
            else:
                for v,r,c in arr:
                    heapq.heappush(heap,(v,r,c))
                
            if y < col-1:
                heapq.heappush(heap, (mat[x][y+1], x, y+1))
            else:        
                return -1
        '''