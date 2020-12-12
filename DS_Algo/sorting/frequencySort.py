'''
1636. Sort Array by Increasing Frequency

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

'''
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        freq = {}
        
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        freqset = set()
        for key, val in freq.items():
            freqset.add(val)
                
        sorted_freq = sorted(freq.items() , key= lambda kv : kv[1])

        freqset = sorted(freqset)
        selected_freq = []

        for fr in freqset:
        
            selected_freq += sorted([k for k,v in sorted_freq if v == fr], reverse=True)
            
        ans = []

        for fr in selected_freq:
            for i in range(freq[fr]):
                ans.append(fr)
            
            
        return ans