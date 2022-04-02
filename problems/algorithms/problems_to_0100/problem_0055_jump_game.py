from typing import List


class Solution:
    # Greedy solution - O(n)
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False

    # slow decision (brute force solution - O(n^n) ) - need cash to improve it
    def canJump2(self, nums: List[int]) -> bool:

        def jump(position):
            if len(nums) - 1 == position:
                return True
            for i in range(nums[position]):
                answer = jump(position + i + 1)
                if answer is True:
                    return True
            else:
                return False
        return jump(0)
