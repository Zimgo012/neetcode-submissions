class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        a = {}

        for i in range(len(nums)):
            diff = target - nums[i] #4,3,2,1
            
            if diff in a.keys():
                return [a.get(diff), i]
            a[nums[i]] = i
            
        return []