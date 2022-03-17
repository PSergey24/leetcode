
class Solution:
    def isHappy(self, n: int) -> bool:
        loopTracker = []

        def getNext(n):
            squares_sum = 0
            numbers = [(n // (10 ** i)) % 10 for i in range(len(str(n)) - 1, -1, -1)]
            for num in numbers:
                squares_sum += num ** 2
            return squares_sum

        while 1:
            n = getNext(n)
            if n == 1:
                return True
            if n in loopTracker:
                return False
            loopTracker.append(n)
