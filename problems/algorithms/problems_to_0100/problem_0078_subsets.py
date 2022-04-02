from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []

        def process(i):
            if i >= len(nums):
                result.append(subset[:])
                return

            subset.append(nums[i])
            process(i+1)

            subset.pop()
            process(i+1)

        process(0)
        return result
