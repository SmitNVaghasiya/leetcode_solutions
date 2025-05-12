class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(digits)
        result = set()

        for a in range(1, 10):     # First digit (no leading 0)
            if count[a] == 0: continue
            count[a] -= 1
            for b in range(0, 10): # Middle digit
                if count[b] == 0: continue
                count[b] -= 1
                for c in range(0, 10, 2): # Last digit (must be even)
                    if count[c] == 0: continue
                    num = a * 100 + b * 10 + c
                    result.add(num)
                count[b] += 1
            count[a] += 1

        return sorted(result)
