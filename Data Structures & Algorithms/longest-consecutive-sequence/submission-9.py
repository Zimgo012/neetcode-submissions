class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seq = set(nums)
        res = 0

        for n in nums:
            if n-1 not in seq:

                l = 1
                while n+l in seq:
                    l += 1
                res = max(res,l)
        return res
