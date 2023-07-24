from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        s1, s2, s3, s4 = -prices[0], float("-inf"), float("-inf"), float("-inf")

        for p in prices:
            s1 = max(s1, -p)
            s2 = max(s2, s1 + p)
            s3 = max(s3, s2 - p)
            s4 = max(s4, s3 + p)

        return max(s4, 0)
