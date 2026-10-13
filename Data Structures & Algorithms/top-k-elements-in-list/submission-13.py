class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        out = [[] for i in range(len(nums) + 1)]
        freq = {}
        
        for n in nums:
            freq[n] = freq.get(n,0) + 1

        for x,y in freq.items():
            out[y].append(x)
        
        res = []

        for i in range(len(out) -1,-1,-1):
            for j in out[i]:
                res.append(j)
                if len(res) == k:
                    return res
        