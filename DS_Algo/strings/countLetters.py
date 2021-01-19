'''
1180. Count Substrings with Only One Distinct Letter: Easy
Q. Given a string S, return the number of substrings that have only one distinct letter.

Example 1:

Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
'''

class Solution:
    def countLetters(self, S: str) -> int:
        
        i, n = 0, len(S)
        count = 0
        
        while i < n:
            idx, c = i, 0         
            while idx< n and S[idx] == S[i]:
                c += 1
                idx += 1
                
            count += c*(c+1)//2

            if idx != i:
                i = idx
            else:
                i += 1
            
        return count