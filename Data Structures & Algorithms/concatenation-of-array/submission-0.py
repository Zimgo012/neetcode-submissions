class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        size = len(nums) * 2 #number of the doubled array

        ans = [0] * size #initialize the size of the new array

        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+len(nums)] = nums[i]

        return ans