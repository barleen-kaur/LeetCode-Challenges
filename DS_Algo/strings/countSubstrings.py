'''
647. Palindromic Substrings: Medium
Q. Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''


class Solution:        
    
    def returnCountCenter(self, string, lo, hi):
        
        ans = 0
        
        while lo >= 0 and hi < len(string):
            
            if string[lo] != string[hi]:
                break
                
            lo -= 1
            hi += 1
            ans += 1
            
        return ans
    
    
    
    def countSubstrings(self, s: str) -> int:
        
        # Incomplete solution! but came up with the algorithm gist pretty well, couldn't code though :p
        # n = len(s)
        # centres = [[-1,1], [0, 1]]
        # count = 0
        # for i in range(n):
        #     print('i: {} count: {}'.format(i, count))
        #     count += 1
        #     for dl,dr in centres:
        #         l,r = max(i+dl,0), min(i+dr,n-1)
        #         print('l: {} r: {} str:{}'.format(l, r, s[l:r+1]))
        #         palindrome = True
        #         while l >= 0 and r < n:
        #             palindrome &= (s[l] == s[r])
        #             if palindrome:
        #                 count += 1
        #             l -= 1
        #             r += 1
        
        
        res = 0
        
        for i in range(len(s)):
            
            res += self.returnCountCenter(s, i, i)
            res += self.returnCountCenter(s, i, i+1)
            
        return res