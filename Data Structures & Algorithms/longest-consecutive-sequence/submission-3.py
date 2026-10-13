class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
  
        oset = set(nums)
        longest = 0

        for o in oset:
            if (o - 1) not in oset:
                length = 1
                while(o + length) in oset:
                    length += 1
                longest = max(length, longest)
        return longest