class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = 1
        if n > 0:
            for i in range(n):
                result = result * x
        else:
            for i in range(n):
                result = result * (1/x)
        return result