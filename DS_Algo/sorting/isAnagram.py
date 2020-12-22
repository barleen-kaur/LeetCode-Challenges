'''
242. Valid Anagram: EASY

Q. Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        #Solution 1: Sorting
        return sorted(s) == sorted(t)
        '''
    
        #Solution 2: Hashing
        
        if len(s) != len(t):
            return False
        
        alphabets = [0]*26
        for st in s:
            alphabets[ord(st)-ord('s')] += 1
        
        for ch in t:
            alphabets[ord(ch)-ord('s')] -= 1
            if alphabets[ord(ch)-ord('s')] < 0:
                return False
        
        return True