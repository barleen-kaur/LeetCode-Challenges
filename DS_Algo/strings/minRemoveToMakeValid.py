'''
1249. Minimum Remove to Make Valid Parentheses: Medium
Q. Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.


Example 2:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
          
        index_to_remove = []
        stack = []
        
        for i, ch in enumerate(s):
            if ch not in '()':
                continue
            if ch == '(':
                stack.append(i)
            elif not stack:
                index_to_remove.append(i)
            else:
                stack.pop()
                
        index_to_remove = set(index_to_remove+stack)
        
        res = []
        for i, ch in enumerate(s):
            if i not in index_to_remove:
                res.append(ch)
                
        return ''.join(res)