'''
557. Reverse Words in a String III: Easy
Q. Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        
        i, n = 0, len(s)
        
        res = ''
        while len(res) < n:
            wstart, wend = i, i+1
            while wend < n and s[wend] != ' ':
                wend += 1
                
            res += s[wstart:wend][::-1] + ' ' if wend < n else s[wstart:wend][::-1]
            i = wend + 1
            
        return res
        