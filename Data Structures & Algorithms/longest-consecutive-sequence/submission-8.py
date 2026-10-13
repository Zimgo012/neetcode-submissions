class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        seq = set(nums)
        res = 0 #longest
        
        for n in nums:

            if n-1 not in seq:

                j = 0
                while (n + j) in seq:
                    j+=1
                res = max(res,j)
        return res
