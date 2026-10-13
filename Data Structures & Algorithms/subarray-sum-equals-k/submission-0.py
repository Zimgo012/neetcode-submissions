class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        currSum = 0
        #initialize map with 1 count of 0
        # prefixSum : count
        prefix = {0 : 1}

        for n in nums:

            #actual sum for prefix
            currSum += n
            diff = currSum - k

            res += prefix.get(diff, 0)
            prefix[currSum] = 1 + prefix.get(currSum, 0)
        
        return res