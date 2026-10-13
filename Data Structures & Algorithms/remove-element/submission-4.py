class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        countE = 0
        l = 0
        r = len(nums) - 1

        while l <= r:

            if nums[l] == val:

                while l <= r and nums[r] == val:
                    r -= 1
                    countE += 1

                # Everything from l onward was val
                if l > r:
                    break

                nums[l], nums[r] = nums[r], nums[l]

                r -= 1
                countE += 1

            l += 1

        for _ in range(countE):
            nums.pop()

        return len(nums)