'''
824. Goat Latin: Easy
Q. A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 
 

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
'''

class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        wordarr = S.split(' ')
        vowels = ('a','e','i','o','u','A','E','I','O','U')
        
        res = ''
        for i, word in enumerate(wordarr):
            if not word.startswith(vowels) and len(word) > 1:
                word = word[1:]+word[0]
            word += 'ma'+('a'*(i+1))
            if i < len(wordarr)-1:
                word += ' '
            res += word
        
        return res
                