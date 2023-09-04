from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        results = [1] * length
        before, after = 1, 1

        for i in range(length):
            results[i] *= before
            before = before*nums[i]
            results[length-i-1] *= after
            after = after*nums[length-i-1]
        return results
