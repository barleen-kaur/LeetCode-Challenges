'''
744. Find Smallest Letter Greater Than Target: Easy
Q. Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:

Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"
'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        low, high = 0, len(letters)-1
        
        while low < high:
            mid = low + (high-low)//2
            
            if letters[mid] > target:
                if letters[low] > target:
                    return letters[low]
                elif letters[low] <= target:
                    high = mid
                    
            elif letters[mid] <= target:
                if letters[high] <= target:
                    return letters[low]
                else:
                    low = mid + 1

        return letters[low]