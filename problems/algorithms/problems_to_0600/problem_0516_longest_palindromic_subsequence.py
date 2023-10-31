class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}

        def dfs(i, j):
            if i < 0 or j == len(s):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            if s[i] == s[j]:
                length = 1 if i == j else 2
                cache[(i, j)] = length + dfs(i - 1, j + 1)
            else:
                cache[(i, j)] = max(dfs(i - 1, j), dfs(i, j + 1))
            return cache[(i, j)]

        for i in range(len(s)):
            dfs(i, i)
            dfs(i, i + 1)
        return max(cache.values())


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for j in range(len(s) + 1)] for i in range(len(s) + 1)]
        res = 0

        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 1 if i == j else 2
                    if i - 1 >= 0:
                        dp[i][j] += dp[i - 1][j + 1]
                else:
                    dp[i][j] = dp[i][j + 1]
                    if i - 1 >= 0:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j])
                res = max(res, dp[i][j])
        return res
