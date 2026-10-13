class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        maxA = -1

        while l < r:

            wd = r - l
            ht = min(heights[l],heights[r])
            maxA = max(maxA, wd * ht)

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            elif heights[l] == heights[r]:
                l+=1
        
        return maxA

