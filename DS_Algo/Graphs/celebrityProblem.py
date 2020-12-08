'''
997. Find the Town Judge/ Celebrity Problem

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.


Example 1:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1


Example 2:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


'''


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        indegree = [0]*N
        outdegree = [0]*N
        
        for edge in trust:
            source = edge[0]-1
            end = edge[1] -1 
            indegree[end] += 1
            outdegree[source] += 1
        
        ans = []
        i = 0
        for indeg, outdeg in zip(indegree, outdegree):
            i += 1
            if indeg == N-1 and outdeg == 0:
                ans.append(i)
            
            
        return ans[0] if len(ans) == 1 else -1
        