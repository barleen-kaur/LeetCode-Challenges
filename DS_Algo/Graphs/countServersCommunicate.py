'''
1267. Count Servers that Communicate

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.

Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
'''


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rowsum = [0]*rows
        colsum = [0]*cols
        
        for i in range(rows):
            rowsum[i] = sum(grid[i])
        
        for i in range(cols):
            colsum[i] =  sum([grid[j][i] for j in range(rows)])
        
        
        row1 = [i for i in range(rows) if rowsum[i] == 1]
        
        c = 0
        for ro in row1:
            colidx = [j for j in range(cols) if grid[ro][j] == 1]
            if colsum[colidx[0]] == 1:
                c += 1
    
        return sum(rowsum) - c
        