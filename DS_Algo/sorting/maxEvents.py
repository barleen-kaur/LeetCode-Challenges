'''
1353. Maximum Number of Events That Can Be Attended: Medium
Q. Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.

Example:

Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4

'''


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        sortevents = sorted(events, key= lambda x: (x[1], x[0]))
        #sortevents = sorted(sortevents, key= lambda x : x[1]-x[0])

        idx = set()
        res = 0
        for st,end in sortevents:
            for d in range(st, end+1):
                if d not in idx:
                    #print(d)
                    res += 1
                    idx.add(d)
                    break
        
        return res