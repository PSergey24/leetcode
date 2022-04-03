from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        idx1 = None

        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                idx1 = i - 1
                break

        if idx1 is not None:
            idx2 = None
            for i in range(n - 1, 0, -1):
                if nums[i] > nums[idx1]:
                    idx2 = i
                    break
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            reverse(idx1 + 1, n - 1)
        else:
            reverse(0, n - 1)
