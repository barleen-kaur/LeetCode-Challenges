'''
1545. Find Kth Bit in Nth Binary String: Medium
Q. Given two positive integers n and k, the binary string  Sn is formed as follows:

S1 = "0"
Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first 4 strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"
Return the kth bit in Sn. It is guaranteed that k is valid for the given n.


Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001". The first bit is "0".

'''


class Solution:
    
    '''
    def invert(self, string):
        invertstr = ['0' if st == '1' else '1' for st in string ]
        return ''.join(invertstr)

    def findKthBit(self, n: int, k: int) -> str:
        i, st = 1, '0'
        
        while i < n:
            st += '1'+ self.invert(st[::-1])
            i += 1
            
        return st[k-1]
    '''
        
    def findKthBit(self, n, k):
        flip = 0
        l = 2 ** n - 1
        print('flip: {}, l: {}'.format(flip, l))
        while k > 1:
            print('k: {}, l: {} flip: {}'.format(k, l, flip))
            if k == l / 2 + 1:
                return str(1 ^ flip)
            if k > l / 2:
                k = l + 1 - k
                flip = 1 - flip
            l /= 2
        return str(flip)