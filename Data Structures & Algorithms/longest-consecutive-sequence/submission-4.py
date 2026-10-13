class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        oset = set(nums)
        longest = 0

        for i in oset:
            if (i-1) not in oset:
                length = 1
                while(i+length) in oset:
                    length += 1
                longest = max(longest, length)
        return longest
