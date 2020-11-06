'''
Q. Number of Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
'''


class Solution:
    def numTrees(self, n: int) -> int:
        def returnBSTs(n):
            if n == 0:
                return 1
            else:
                sol = 0
                for root in range(1, n+1):
                    sol += returnBSTs(root-1)*returnBSTs(n-root)
            return sol
               
    return returnBSTs(n) if n > 0 else 0