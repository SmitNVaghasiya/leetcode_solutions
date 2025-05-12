class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        power = 1
        while power <= n:
            if power == n:
                return True
            power = power * 3
        return False