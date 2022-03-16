
# https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        numbers_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        flag = False
        for i in range(len(s)):
            if flag is not True:
                current_value = numbers_dict[s[i]]
                if i != (len(s)-1):
                    next_value = numbers_dict[s[i+1]]
                    if int(next_value/current_value) in [5, 10] and i != (len(s)-1):
                        total += (next_value - current_value)
                        flag = True
                    else:
                        total += current_value
                else:
                    total += current_value
            else:
                flag = False
        return total
