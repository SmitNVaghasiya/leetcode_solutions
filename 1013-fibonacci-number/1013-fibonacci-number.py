class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b