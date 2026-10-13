class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record = []

        for i in operations:

            match i:
                case "+":
                    a = record[-1]
                    b= record[-2]
                    record.append(a + b)
                case "D":
                    c = record[-1]
                    record.append(c * 2)
                case "C":
                    record.pop()
                case _:
                    record.append(int(i))
        
        sumR = 0

        for j in range(len(record)):
            sumR += record[j]

        
        return sumR

