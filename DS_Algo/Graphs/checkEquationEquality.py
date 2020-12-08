'''
Q. Satisfiability of Equality Equations
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

Example:
Input: ["a==b","b!=c","c==a"]
Output: false
'''


class Solution:
    
    parent = list(range(26))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) 
        return self.parent[x]
    
    def union(self, x, y):
        parX = self.find(x)
        parY = self.find(y)
        self.parent[parY] = parX
        
        
    def check(self, x, y):
        return self.find(x) == self.find(y)
            
    def equationsPossible(self, equations: List[str]) -> bool:
        
        for eq in equations:
            if eq[1] == '=':
                node1 = ord(eq[0])-ord('a')
                node2 = ord(eq[-1])-ord('a')
                par1 = self.find(node1)
                par2 = self.find(node2)
                if par1 != par2:
                    self.union(node1, node2)
    
        
        for eq in equations:
            if eq[1] == '!':
                node1 = ord(eq[0])-ord('a')
                node2 = ord(eq[-1])-ord('a')
                par1 = self.find(node1)
                par2 = self.find(node2)
                if par1 == par2:
                    return False
        
        return True
        