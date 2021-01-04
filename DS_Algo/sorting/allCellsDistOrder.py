'''
1030. Matrix Cells in Distance Order: Easy
Q. We are given a matrix with R rows and C columns has cells with integer coordinates (r, c), where 0 <= r < R and 0 <= c < C.

Additionally, we are given a cell in that matrix with coordinates (r0, c0).

Return the coordinates of all cells in the matrix, sorted by their distance from (r0, c0) from smallest distance to largest distance.  Here, the distance between two cells (r1, c1) and (r2, c2) is the Manhattan distance, |r1 - r2| + |c1 - c2|.  (You may return the answer in any order that satisfies this condition.)

Example 1:

Input: R = 1, C = 2, r0 = 0, c0 = 0
Output: [[0,0],[0,1]]
Explanation: The distances from (r0, c0) to other cells are: [0,1]


Example 2:
Input: R = 2, C = 2, r0 = 0, c0 = 1
Output: [[0,1],[0,0],[1,1],[1,0]]
Explanation: The distances from (r0, c0) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.

'''

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        
        '''
        #Solution 1 : Brute Force: Sorting
        dict_ = {(i,j): 0 for i in range(R) for j in range(C)}

        for i,j in dict_.keys():
            dict_[i,j] = abs(r0-i) + abs(c0-j)
            
        sorteddict = sorted(dict_.items(), key = lambda kv: kv[1])
        
        return [kv[0] for kv in sorteddict]
    
        '''
        
        #Solution 2 : BFS
        queue = [[r0,c0, 0]]
        visited = set([(r0,c0)])
        ans = []
        while queue:
            nextlvl = []
            for i in range(len(queue)):
                x, y, dist = queue[i]
                ans.append([x, y])
                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                for dx, dy in directions:
                    new_x, new_y = x+dx, y+dy
                    if 0 <= new_x < R and 0 <= new_y < C and (new_x,new_y) not in visited:
                        visited.add((new_x, new_y))
                        nextlvl.append([new_x, new_y, dist+1])
            queue = nextlvl
        return ans