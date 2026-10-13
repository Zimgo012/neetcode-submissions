class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        

        bxs = list(boxes)
        res = [0 for i in range(len(bxs))]

        balls = 0
        moves = 0
        for i in range(len(bxs)):

            res[i] = balls + moves
            moves += balls

            if int(bxs[i]) == 1:
                balls += 1
        
        balls = 0
        moves = 0
        for i in range (len(bxs) -1,-1,-1):
            res[i] = res[i] + balls + moves
            moves += balls

            if int(bxs[i]) == 1:
                balls += 1
                        
        return res
            
    