from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        if len(digits) == 0:
            return results

        numbers = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        row = ""

        def process(n, current_row):
            if len(current_row) == len(digits):
                results.append(current_row)
                return

            current_string = numbers[int(digits[n])]
            for j in range(len(current_string)):
                current_row += current_string[j]
                process(n+1, current_row)
                current_row = current_row[:-1]

        process(0, row)
        return results
