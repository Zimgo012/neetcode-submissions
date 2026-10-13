class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = 1 + count.get(i,0)
        
        for key , v in count.items():
            freq[v].append(key)
        
        res = []

        for r in range(len(freq) - 1, 0, -1):
            for n in freq[r]:
                res.append(n)
                if len(res) == k:
                    return res
            
