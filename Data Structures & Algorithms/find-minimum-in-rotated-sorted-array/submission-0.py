class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = nums[0]
        l = 0 
        r = len(nums) - 1

        while l <= r:

            #if the array is rotated back in into its original 
            #position where first element is lesser than last element
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l +r) // 2
            res = min (res,nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
