'''
1129. Shortest Path with Alternating Colors

Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

 

Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
'''

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        path = [-1 for _ in range(n)]
        path[0] = 0
        
        adj_list = {i: [] for i in range(n)}
        
        for st, end in red_edges:
            adj_list[st].append((end, 'r'))
        for st, end in blue_edges:
            adj_list[st].append((end, 'b'))    
            
        queue = []
        
        for nextnode, color in adj_list[0]:
            queue.append((nextnode, color))
        
        visited = {(0,'r'), (0, 'b')}
        level = 0
        
        while queue:
            
            level += 1
            
            nextqueue = []
            for node, color in queue:
                visited.add((node, color))
                if path[node] == -1:
                    path[node] = level
                else:
                    path[node] = min(path[node], level)
                    
                for nextnode, nextcolor in adj_list[node]:
                    
                    if nextcolor != color and (nextnode, nextcolor) not in visited:
                        nextqueue.append((nextnode, nextcolor))
                        visited.add((nextnode, nextcolor))
            
            queue = nextqueue
            
