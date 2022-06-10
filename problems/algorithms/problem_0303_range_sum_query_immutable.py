from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sumMat = [0] * (len(nums) + 1)

        prefix = 0
        for c in range(len(nums)):
            prefix += nums[c]
            self.sumMat[c + 1] = prefix

    def sumRange(self, left: int, right: int) -> int:
        return self.sumMat[right + 1] - self.sumMat[left]

