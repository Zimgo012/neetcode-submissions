class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        ans = [0] * len(arr)
        highestR = -1

        for i in range(len(arr) - 1, -1, -1):
            ans[i] = highestR
            highestR = max(highestR, arr[i])
        return ans

            

