'''
797. All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

'''


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        
        pathlst = []
        
        def dfs(path, node):
            
            if node == n-1:
                pathlst.append(list(path))
                return 
        
            for nextNode in graph[node]:
                path.append(nextNode)
                dfs(path, nextNode)
                path.pop()
          
        
        path = [0]
        dfs(path, 0)
        return pathlst