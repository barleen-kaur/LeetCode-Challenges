955. Delete Columns to Make Sorted II: Medium

Q. We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef","vyz"].

Suppose we chose a set of deletion indices D such that after deletions, the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).

Return the minimum possible value of D.length.

 

Example 1:

Input: ["ca","bb","ac"]
Output: 1
Explanation: 
After deleting the first column, A = ["a", "b", "c"].
Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
'''


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        
        n = len(A)
        if A == []:
            return 0
        
        n_str = len(A[0])
        count = 0
        
        preflag = [False]*(len(A)-1) + [True]
        for j in range(n_str):
            currflag = [False]*(len(A)-1) + [True]
            flag = True
            for i in range(n-1):
                if all(preflag[i] for i in range(len(A))):
                    return count
                elif not preflag[i]:
                    if A[i][j] < A[i+1][j]:
                        currflag[i] = True
                    elif A[i][j] == A[i+1][j]:
                        continue
                    else:
                        flag = False
                        
                else:
                    if A[i][j] < A[i+1][j] or A[i][j] > A[i+1][j]:
                        currflag[i] = True
            
            if not flag:
                count += 1
            else:
                preflag = [preflag[i] or currflag[i] for i in range(len(A))]        
        return count
