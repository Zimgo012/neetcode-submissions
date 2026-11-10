class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        # piles -> [i,i,i,i]
        # i -> number of banana

        # h -> represenst the number of hrs you have to eat all banana
        # example: given 3, 3 hrs -> to eat all banana

        # k = eating rate
        # example : 3 bananas / hr

        # [1,4,3,2] h = 9
        # 1 - 10 hrs to finish
        # 2 - 6 hrs || minimum rate
        # 3 - 5 hrs 
        # 4 - 4 hrs || max rate


        # k = [1,2,3,4]

        #[0,1,3,6,10]

        # l = [10,9,7,4]
        # a = 10 sum of bananas in pile

        # naive way 
        # 1. [1, 2 ,3 ,4]
        # 2. 1 per pile -> 2p per pile .. max per pile
        # 3. check how many items we tried <= hrs needed to complete to eat the pile of bananas
        # check he minimum then return it

        # effiecient way
        # 1. [1,2,3,4]
        # 2. [1,2,3 (m),4] = 5  h = 6 a < 6
        # 3  [1,2(m),3 -] = 6  h = 6 a < 6 return 6
        # 1 / 2 = 0.5 -> 1

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            
            if hours <= h:
                res = min(res , m)
                r = m - 1
            else:
                l = m + 1

        return res






        

