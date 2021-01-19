'''
1347. Minimum Number of Steps to Make Two Strings Anagram: Medium
Q. Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
'''

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        sdict = collections.Counter(s)
        tdict = collections.Counter(t)
        
        count = 0
        
        for ch in s:
            if ch in tdict:
                tdict[ch] -= 1
                if tdict[ch] == 0:
                    del tdict[ch]
            else:
                count += 1
                
        return count
                