class Solution:
    def isHappy(self, n: int) -> bool:
        
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)
            slow = self.sumOfSquares(slow)
        
        if fast == 1:
            return True
        else:
            return False

    def sumOfSquares(self, n):
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output