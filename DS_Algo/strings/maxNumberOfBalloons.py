'''
1189. Maximum Number of Balloons: Easy
Q. Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
 

Example 1:

Input: text = "nlaebolko"
Output: 1
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        freq = collections.Counter(text)
        
        count = 0
        while True:
            for ch in 'balloon':
                if freq[ch]:
                    freq[ch] -=1
                else:
                    return count
                if ch == 'n':
                    count += 1