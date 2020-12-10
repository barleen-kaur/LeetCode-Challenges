'''
1615. Maximal Network Rank

There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.

'''

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        if len(roads) < 1:
            return 0
        
        indegree = [0]*n
        
        for st, end in roads:
            indegree[st] += 1
            indegree[end] += 1
        
        val = max(indegree)
        keys = [i for i in range(n) if indegree[i] == val]
        

        max_rank = 0
        
        if len(keys) > 1:
            for i, ik in enumerate(keys):
                for j, jk in enumerate(keys[i+1:]):
                    if [ik, jk] in roads or [jk, ik] in roads:
                        rank = indegree[ik] + indegree[jk] - 1
                    else:
                        rank = indegree[ik] + indegree[jk]
                    max_rank = max(rank, max_rank)
            return max_rank
        
        else:
            first = indegree[keys[0]]
            indegree[keys[0]] = 0
            val = max(indegree)
            key2 = [i for i in range(n) if indegree[i] == val]
            max_rank = 0
            for i in key2:
                if [i, keys[0]] in roads or [keys[0], i] in roads:
                    rank = indegree[i] + first - 1
                else:
                    rank = indegree[i] + first

                max_rank = max(rank, max_rank)
                
            return max_rank
            