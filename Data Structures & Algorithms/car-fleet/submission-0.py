class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        newarray = list(zip(position, speed))
        newarray.sort(reverse=True)


        stack = []

        for x,y in newarray:
            time = (target - x) / y
            
            if stack:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)
    