'''
Q.  Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
'''


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        dist = {node : float('inf') for node in range(1,N+1)}
        dist[K] = 0        
        
        graph = collections.defaultdict(list) 
        for u, v, w in times:
            graph[u] += [(v,w)]
            
        seen = [False]*(N+1)
        n = 0
        while n < N:
            
            min_val = float('inf')
            idx = -1
            for i in range(1, N+1):
                if not seen[i] and dist[i] < min_val:
                        min_val = dist[i]
                        idx = i

            if idx == -1:
                return -1
            else:
                seen[idx] = True
                n += 1
                for nei, wei in graph[idx]:
                    dist[nei] = min(dist[nei], dist[idx] + wei)
                
        ans = max(dist.values()) 
        return -1 if ans == float('inf') else ans