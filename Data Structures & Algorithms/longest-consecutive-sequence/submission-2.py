class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        longest = 0
        oset = set(nums)

        for i in nums:
            if (i-1) not in oset:
                length = 0
                
                while (i + length) in oset:
                    length += 1
                longest = max (length, longest)
        
        return longest