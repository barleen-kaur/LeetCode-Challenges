'''
1221. Split a String in Balanced Strings: Easy
Q. Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.


Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
'''

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        l,r = 0,0
        i,n = 0, len(s)
        count = 0
        
        while i < n:
            
            
            if s[i] == 'L':
                l += 1
                
            elif s[i] == 'R':
                r += 1
            
            if l == r and l != 0 and r != 0:
                count += 1
                l = 0
                r = 0
                
            i += 1
            
        return count