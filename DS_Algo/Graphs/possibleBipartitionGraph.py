'''
886. Possible Bipartition

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

'''


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        grp = [-1 for _ in range(N)]
        
        adj_list = {i: [] for i in range(N)}
        for x, y in dislikes:
            adj_list[x-1].append(y-1)
            adj_list[y-1].append(x-1)

        
        def dfs(node, flag):
            if grp[node] == -1:
                grp[node] = flag
            
            for nei in adj_list[node]:
                if grp[nei] == -1:
                    dfs(nei, 1-flag)
                    
                else:
                    if grp[nei] != 1-flag:
                        grp[nei] = float('inf')
                    
        
        flag = 0
        for node, neighbor in adj_list.items():

            if grp[node] == -1:
                grp[node] = flag
            
                for nei in neighbor:
                    dfs(nei, 1-flag)
            
                    
        return False if any(i == float('inf') for i in grp) else True
        