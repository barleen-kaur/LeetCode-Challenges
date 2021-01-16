'''
911. Online Election: Medium
Q. In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

 

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
'''


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.leader = []
        
        count = collections.Counter() 
        lead, maxvote = None, 0
        
        for p,t in zip(self.persons, self.times):
            count[p] += 1
            if count[p] >= maxvote:
                maxvote = count[p]
                lead = p
            self.leader.append((t, lead))
                

    def q(self, t: int) -> int:
        #print(self.leader)
        low, high = 0, len(self.times)-1
        
        while low < high:
            
            mid = low + (high-low)//2
            curr = self.times[mid]
            
            if curr == t:
                low = mid + 1
                break
            elif curr < t:
                low = mid + 1 
            else:
                high = mid - 1
         
        if self.times[low] > t:
            return self.leader[low-1][1]
        else:
            return self.leader[low][1]
        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)