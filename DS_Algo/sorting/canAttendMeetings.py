'''
252. Meeting Rooms: Easy
Q. Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true

'''


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key= lambda x:x[1])
        for i in range(len(intervals)-1):
            end = intervals[i][1]
            st = intervals[i+1][0]
            if end > st:
                return False
            
        return True