from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = 1
        for i in range(len(digits)-1, -1, -1):
            current_sum = digits[i] + integer
            integer = current_sum // 10
            digits[i] = current_sum % 10
        if integer > 0:
            digits.insert(0, integer)
        return digits
