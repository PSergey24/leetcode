from collections import defaultdict


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(i):
            nonlocal ans
            if i == n:
                ans += 1
                return ans

            for j in range(n):
                if not cols[j] and not diagonals[i + j] and not antiDiagonals[i - j]:
                    cols[j] = True
                    diagonals[i + j] = True
                    antiDiagonals[i - j] = True

                    backtrack(i + 1)

                    cols[j] = False
                    diagonals[i + j] = False
                    antiDiagonals[i - j] = False

        cols = [False] * n
        diagonals = defaultdict(bool)
        antiDiagonals = defaultdict(bool)
        ans = 0

        backtrack(0)
        return ans
