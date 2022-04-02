

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"(": ")", "[": "]", "{": "}"}
        stack = []

        for symbol in s:
            if symbol in parentheses:
                stack.append(parentheses[symbol])
            else:
                if len(stack) == 0 or len(stack) > 0 and stack.pop() != symbol:
                    return False
        return True if len(stack) == 0 else False
