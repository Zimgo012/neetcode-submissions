class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxc = 0
        c = 0

        for i in nums:
            if i == 1:
                c += 1
                maxc = max(maxc,c)
            else:
                c =0
        return maxc
        

