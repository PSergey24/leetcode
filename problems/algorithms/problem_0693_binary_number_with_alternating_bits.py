class Solution:
    def hasAlternatingBits2(self, n: int) -> bool:
        last = n % 2
        n >>= 1
        while n > 0:
            current = n % 2
            if current == last:
                return False
            last = current
            n >>= 1
        return True

    def hasAlternatingBits(self, n: int) -> bool:
        if not n:
            return True

        num = n ^ (n >> 1)
        return not num & (num + 1)
