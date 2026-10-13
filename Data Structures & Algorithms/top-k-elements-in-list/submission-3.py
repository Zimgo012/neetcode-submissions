class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for c in nums:
            count[c] = 1 + count.get(c,0)
        
        for key, v in count.items():
            freq[v].append(key)

    
        res = []

        for i in range(len(freq) -1,0,-1):
            for f in freq[i]:
                res.append(f)
                if len(res) == k:
                    return res
