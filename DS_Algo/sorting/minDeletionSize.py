'''
944. Delete Columns to Make Sorted: Easy

Q. We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"], and the remaining columns of A are ["b","v"], ["e","y"], and ["f","z"].  (Formally, the c-th column is [A[0][c], A[1][c], ..., A[A.length-1][c]]).

Suppose we chose a set of deletion indices D such that after deletions, each remaining column in A is in non-decreasing sorted order.

Return the minimum possible value of D.length.


Example 1:

Input: A = ["cba","daf","ghi"]
Output: 1
Explanation: 
After choosing D = {1}, each column ["c","d","g"] and ["a","f","i"] are in non-decreasing sorted order.
If we chose D = {}, then a column ["b","a","h"] would not be in non-decreasing sorted order.

'''

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        
        n = len(A)
        if A == []:
            return 0
        
        n_str = len(A[0])
        count = 0
        
        for j in range(n_str):
            max_ch = ord('a')
            for i in range(n):
                if ord(A[i][j]) < max_ch:
                    count += 1
                    break
                else:
                    max_ch = max(max_ch, ord(A[i][j]))
        
        return count