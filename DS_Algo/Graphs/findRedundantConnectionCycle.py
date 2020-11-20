'''
Q. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:

Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
'''
class Solution:

    def find(self, node):
        
        if self.parent[node] >= 0:
            return self.find(self.parent[node])
        
        return node, self.parent[node]
            
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # Set: Union and Find
        n = len(edges)
        self.parent = [-1]*n
        
        for u, v in edges:
            u = u-1
            v = v-1
            par_u, rank_u = self.find(u)
            par_v, rank_v = self.find(v)

            if par_u != par_v:
                if rank_v < rank_u:
                    self.parent[u] = par_v
                    self.parent[par_u] = par_v
                    self.parent[par_v] -= rank_u
                else:
                    self.parent[v] = par_u
                    self.parent[par_v] = par_u
                    if rank_v > 0:
                        self.parent[par_u] -= rank_v  
                    else:
                        self.parent[par_u] -= -rank_v
            else:
                return u+1,v+1

    '''            
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # Topological solution Lengthy: not very impressive! :p
        n = len(edges)
        indegree = {} 
        neighbors = {}
        for pre, suc in edges:
            if pre not in indegree:
                neighbors[pre] = [suc]
                indegree[pre] = 1
            else:
                neighbors[pre].append(suc)
                indegree[pre] += 1
                
            if suc not in indegree:
                neighbors[suc] = [pre]
                indegree[suc] = 1
            else:
                neighbors[suc].append(pre)
                indegree[suc] += 1

        min_deg = min(indegree.values())

        if min_deg != 1:
            return edges[-1]
        else:
            queue = []
            for i in range(1,n+1):
                if indegree[i] == 1:
                    queue.append(i)

        while queue:
            curr = queue.pop(0)
            
            for nei in neighbors[curr]:
                neighbors[nei].remove(curr)
                indegree[nei] -= 1
                if indegree[nei] == 1:
                    queue.append(nei)
            
            indegree.pop(curr)
            min_deg = min(indegree.values())
            
            if min_deg != 1:
                break
            
        
        key = indegree.keys()
        ans = []
        for pre, suc in edges:
            if pre in key and suc in key:
                ans = [pre,suc]
    
        return ans
    '''

