'''
392. Is Subsequence: Easy
Q. Given a string s and a string t, check if s is subsequence of t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
'''


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        '''
        # Solution 1: Dynamic Programming: O(nm)
        tab = [[0]*(len(t)+1) for i in range(len(s)+1)]
        
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    tab[i+1][j+1] = max(tab[i][j+1], tab[i+1][j], tab[i][j]+1)
                    
                else:
                    tab[i+1][j+1] = max(tab[i][j+1], tab[i+1][j], tab[i][j])
        
        print(tab)
        return len(s) == tab[-1][-1]
        '''
        
        #Solution 2: linear search: 0(max(m,n))
        s_low, s_high = 0, len(s)
        t_low, t_high = 0, len(t)
        
        while s_low < s_high and t_low < t_high:
            #print('S[{}]:{}, T[{}]:{}'.format(s_low, s[s_low], t_low, t[t_low]))
            if s[s_low] == t[t_low]:
                s_low += 1
                
            
            t_low +=1
            
        return s_low == s_high

        