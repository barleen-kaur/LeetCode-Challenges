'''
Q. Minimum Height Trees

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

'''


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        #   Brute Force Code: Time Limit Exceeded :(
        neighbors = [[] for i in range(n)]
        for edge in edges:
            a, b = edge[0], edge[1]
            neighbors[a].append(b)
            neighbors[b].append(a)
            
        entry = {}
        global max_depth
        max_depth = 0 
        def minHeightTrees(start, curr, depth, arr):
            global max_depth
            
            if depth == 0:
                for i in range(n):
                    arr = []
                    max_depth = 0 
                    for nei in neighbors[i]:
                        if nei not in arr and nei != i:
                            arr.append(nei)
                            minHeightTrees(i, nei, depth+1, arr)   
                    entry[i] = max_depth
                    
            else:
                for nei in neighbors[curr]:
                    if nei not in arr and nei != start:
                        arr.append(nei)
                        minHeightTrees(start, nei, depth+1, arr)       
                max_depth = max(max_depth, depth)

        
        arr = []
        minHeightTrees(0, 0, 0, arr)
        min_val = min(entry.values())
        return [key for key, val in entry.items() if entry[key] == min_val]  
        '''

        # Topological Sorting

        if n < 1:
            return []
        elif n == 1:
            return [0]
        
        neighbors = [[] for i in range(n)]
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        leaves = []
        
        for i, nei in enumerate(neighbors):
            if len(nei) == 1:
                leaves.append(i)
        
        count = n
        
        while count > 2:
            count -= len(leaves)
            
            for _ in range(len(leaves)):
                
                leaf = leaves.pop(0)
                                
                for i in range(len(neighbors[leaf])):
                    nei = neighbors[leaf].pop(0)
                    neighbors[nei].remove(leaf)
                    
                    if len(neighbors[nei]) == 1:
                        leaves.append(nei)
        
        return leaves
                

