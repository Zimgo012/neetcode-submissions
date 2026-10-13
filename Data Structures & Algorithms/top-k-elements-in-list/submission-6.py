class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        frequency = [ [] for i in range(len(nums) + 1)]

        print(frequency)
        
        for i in nums:
            count[i] = 1 + count.get(i,0)
        print(count)

        for key, val in count.items():
            frequency[val].append(key)
        print(frequency)
        
        res = []
        for i in range(len(frequency) -1, 0, -1):
            for e in frequency[i]:
                res.append(e)
                if len(res) == k:
                    return res
