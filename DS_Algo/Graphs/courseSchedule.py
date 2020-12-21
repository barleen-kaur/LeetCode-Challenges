'''
Q. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.

'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0] * numCourses
        
        for entry in prerequisites:
            pre, suc = entry[0], entry[1]
            indegree[suc] += 1
        
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                
        topo = []       
        while queue:
            course = queue.pop(0)
            topo.append(course)
            
            for entry in prerequisites:
                pre, suc = entry[0], entry[1]
                if pre == course:
                    indegree[suc] -= 1
                    if indegree[suc] == 0:
                        queue.append(suc)
    
        return len(topo) == numCourses