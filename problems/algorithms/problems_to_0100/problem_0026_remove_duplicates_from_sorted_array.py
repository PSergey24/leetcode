from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        r = 1

        for i in range(r, len(nums), 1):
            if nums[i] != nums[i - 1]:
                nums[l] = nums[i]
                l += 1
        return l

