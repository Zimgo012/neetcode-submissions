class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []

        hashm = {}

        for i in nums:
            hashm[i] = hashm[i] + 1 if i in hashm else 1

        sorted_keys = sorted(hashm, key=hashm.get, reverse=True)

        return  sorted_keys[:k]   