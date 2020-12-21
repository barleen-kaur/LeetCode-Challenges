'''
451. Sort Characters By Frequency : Medium
Q. Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        
        chdict = {}
        for ch in s:
            if ch not in chdict:
                chdict[ch] = 1
            else:
                chdict[ch] += 1
                
        sorteddict = sorted(chdict.items(), key= lambda k:k[1], reverse=True)
        print(sorteddict)
        
        string = ''
        for ch, freq in sorteddict:
                string += ch*freq
                
        return string