'''
1162. As Far from Land as Possible

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
'''

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        max_min_dist = -1
        queue = []
        
        for X in range(rows):
            for Y in range(cols):
                if grid[X][Y] == 1:
                    visited[X][Y] = True
                    for dx, dy in [[-1,0],[0,1],[1,0],[0,-1]]:
                        newX, newY = X + dx, Y + dy
                        if 0 <= newX < rows and 0 <= newY < cols and not visited[newX][newY] and grid[newX][newY] == 0:
                            queue.append((newX, newY, 1))
                            visited[newX][newY] = True
                            
        
        while queue:
            
            X, Y, dist = queue.pop(0)
            
            max_min_dist = max(max_min_dist, dist)
            
            for dx, dy in [[-1,0],[0,1],[1,0],[0,-1]]:
                newX, newY = X + dx, Y + dy
                if 0 <= newX < rows and 0 <= newY < cols and not visited[newX][newY] and grid[newX][newY] == 0:
                    queue.append((newX, newY, dist+1))
                    visited[newX][newY] = True
                    
        return max_min_dist