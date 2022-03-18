from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for n in nums:
            answer = answer ^ n
        return answer
