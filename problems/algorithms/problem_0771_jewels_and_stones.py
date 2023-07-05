class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        check_j = set(jewels)
        total = 0
        for st in stones:
            if st in check_j:
                total += 1
        return total
