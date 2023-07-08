class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n in [1, 2]:
            return 1

        two = [1, 1]

        def rec(n):
            if n == 2:
                return

            two.append(sum(two))
            two.pop(0)
            rec(n - 1)

        rec(n)
        return two[-1]
