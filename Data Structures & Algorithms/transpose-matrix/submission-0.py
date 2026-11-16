class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows = len(matrix) #2
        cols = len(matrix[0]) #3

        res = [[0] * rows for _ in range (cols)]  # 2 x 3

        for r in range(rows):
            for c in range(cols):
                res[c][r] = matrix[r][c]
        
        return res

