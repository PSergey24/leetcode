from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []

        results = []
        count = {"(": n, ")": n}
        cur_string = ""

        def generateItem(current_string, res):
            if len(current_string) == n * 2:
                res.append(current_string[:])
                return res

            for parenthesis in count:
                if count[parenthesis] > 0:
                    if parenthesis == ")" and count[parenthesis] - 1 >= count["("] or parenthesis == "(":
                        current_string += parenthesis
                    count[parenthesis] -= 1

                    res = generateItem(current_string, res)

                    count[parenthesis] += 1
                    current_string = current_string[:-1]
            return res

        results = generateItem(cur_string, results)
        return results
