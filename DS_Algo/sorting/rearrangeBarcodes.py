'''
1054. Distant Barcodes: Medium
Q. In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
'''
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
    
        n = len(barcodes)
        if n < 2:
            return barcodes
        
        dict_ = collections.Counter(barcodes)

        heap = []
        for key in dict_:
            heap.append((-dict_[key], key))
    
        heapq.heapify(heap)
        
        ans = []
        while len(ans) < n:
            ffreq, fst = heapq.heappop(heap)
            if not ans or ans[-1] != fst:
                ans.append(fst)
                if ffreq != -1:
                    heapq.heappush(heap, (ffreq+1, fst))     
            else:
                sfreq, sec = heapq.heappop(heap)
                ans.append(sec)
                if sfreq != -1:
                    heapq.heappush(heap, (sfreq+1, sec))  
                heapq.heappush(heap, (ffreq, fst))  
                
        return ans
            
            
            
            