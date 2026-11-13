class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # nums = [1,2,2,3,3,4,5]
        # [][1][2][3][1][1]
        # 0 1   2  3 4   5

        # [1,2,3,3,100]
        # [] x 100


      
        
        out = [[] for i in range(len(nums) + 1)]
        freq = {}

        # how many times did that number appeared in the array
        #ex. 1 -> 3
        #.   2 -> 1
        for n in nums:
            freq[n] = freq.get(n,0) + 1
        

        # [][1,2,100][3][][][]
        # 0 1         2  3 
        for x,y in freq.items():
            out[y].append(x)

        # top frequency
        # <-----------------
        res = []
        for i in range(len(out) -1, 0, -1):
            for n in out[i]:
                res.append(n)
                if len(res) == k:
                    return res

        





