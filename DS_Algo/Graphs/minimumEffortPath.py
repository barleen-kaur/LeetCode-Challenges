'''
1631. Path With Minimum Effort

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
'''



class Solution:
    
    graph = {}
    def return_graph(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                node = cols*i + j
                self.graph[node] = self.return_neighbors(i,j, matrix)
    
    def return_neighbors(self, i,j, matrix):
        
        indices = [(i-1,j),(i,j-1),(i,j+1), (i+1, j)]
        N = len(matrix)
        neighbors = []
        for m,n in indices:
            if m < N and m >= 0 and n < N and n >= 0:
                nei = N*m + n
                #print('i: {}, j: {}, m: {}, n: {}, nei: {}'.format(i,j,m,n,nei))
                neighbors.append((nei,abs(matrix[m][n] - matrix[i][j])))
        
        return neighbors
    
    def dijsktra(self):
        arr = [-float('inf')]*len(self.graph.keys())
        visited = [False]*len(self.graph.keys())
        arr[0] = 0
        queue = [(0, 0)]
        #print(self.graph)
        while queue:
    
            diff, node = heapq.heappop(queue)

            visited[node] = True
            for nei, cost in self.graph[node]:
                if not visited[nei]:
                    if arr[nei] < 0:
                        arr[nei] = max(arr[node], cost)
                    else:
                        arr[nei] = min(arr[nei], max(arr[node], cost))
                    heapq.heappush(queue, (arr[nei], nei))
            #print('node: {}, arr: {}'.format(node, arr))
                    
        return arr 
                    
                
                
        
        
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        self.return_graph(heights)
        cost = self.dijsktra()

        return cost[-1]
        
        
        
        
        
        
        