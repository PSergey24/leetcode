from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            nums.insert(0, nums.pop())


# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:

#         if k >= len(nums):
#             k = k%len(nums)
#         if len(nums)==1 or k == 0:
#             return nums
#         nums[:k], nums[k:] = nums[-k:], nums[:-k]
#         return nums
