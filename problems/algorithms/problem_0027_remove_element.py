import copy
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums)
        count = len(nums)

        for j in range(r, 0, -1):
            for i in range(l, j, 1):
                if nums[i] == val:
                    k = copy.copy(nums[j-1])
                    nums[i] = k
                    nums[j-1] = 111
                    count -= 1
                    break
        return count


