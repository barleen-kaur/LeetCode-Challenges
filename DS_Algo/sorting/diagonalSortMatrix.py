'''
1329. Sort the Matrix Diagonally: Medium
Q. A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Example 1:

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
'''


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows, cols = len(mat), len(mat[0])
        
        coords = [[i, 0] for i in range(rows)] + [[0,i] for i in range(1,cols)]
        
        diagdict = {i-j: [] for i,j in coords}
        
        for i, j in coords:
            diagdict[i-j] += [mat[i][j]]
            while i+1 < rows and j+1 < cols:
                diagdict[i-j] += [mat[i+1][j+1]]
                i += 1
                j += 1
                
        for key, val in diagdict.items():
            diagdict[key] = sorted(val)
        
        for i, j in coords:
            mat[i][j] = diagdict[i-j][0]
            k = 1
            while i+1 < rows and j+1 < cols:
                mat[i+1][j+1] = diagdict[i-j][k]
                i += 1
                j += 1
                k += 1
                
        return mat