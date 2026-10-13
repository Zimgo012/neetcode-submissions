class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashM = {}
        res = []

        for i in range(len(nums)):

            diff = target - nums[i]
            
            if diff in hashM:
                res.append(hashM[diff])
                res.append(i)

            hashM[nums[i]] = i

        print(hashM)
        return res

