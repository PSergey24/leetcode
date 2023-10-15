from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        sumWindow = 0
        res = float('inf')

        for right in range(len(nums)):
            sumWindow += nums[right]

            while sumWindow >= target:
                res = min(res, right-left+1)
                sumWindow -= nums[left]
                left += 1
        return res if res != float('inf') else 0
