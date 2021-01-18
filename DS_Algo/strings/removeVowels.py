'''
1119. Remove Vowels from a String: Easy

Q. Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:

Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: s = "aeiou"
Output: ""
'''


class Solution:
    def removeVowels(self, s: str) -> str:
        
        '''
        # Solution 1: BruteForce : O(n^2)
        newstr = '' 
        vowels = ['a','e','i','o','u']
        
        for ch in s:
            if ch not in vowels:
                newstr += ch
                
        return newstr
        '''    
            
        vowels = ['a','e','i','o','u']    
        return ''.join(ch for ch in s if ch not in vowels)