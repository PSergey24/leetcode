from typing import List


class Solution:
    # faster
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0 for r in range(len(nums))] for l in range(len(nums))]
        for l in range(len(nums) - 2, 0, -1):
            for r in range(1, len(nums) - 1):
                if l <= r:
                    dp[l][r] = max(
                        nums[l - 1] * nums[i] * nums[r + 1] + dp[l][i - 1] + dp[i + 1][r] for i in range(l, r + 1))
        return max(y[-2] for y in dp)

    # little bit slower
    def maxCoins2(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}

        def process(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += process(l, i - 1) + process(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
        return process(1, len(nums) - 2)

    # brute-force solution - time = O(n^n)
    def maxCoins3(self, nums: List[int]) -> int:
        sum = 0
        results = []

        def process(currentSum):
            if len(nums) == 0:
                results.append(currentSum)
                return

            for i in range(len(nums)):
                previousNum = nums[i - 1] if i - 1 >= 0 else 1
                nextNum = nums[i + 1] if i + 1 < len(nums) else 1
                currentValue = previousNum * nums[i] * nextNum
                n = nums.pop(i)
                currentSum += currentValue
                process(currentSum)
                currentSum -= currentValue
                nums.insert(i, n)
        process(sum)
        return max(results)
