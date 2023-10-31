
class Solution:
    def decodeString(self, s: str) -> str:

        k = 0
        cur_str = ""
        stack = []
        for char in s:

            if char.isdigit():
                k = 10 *k + int(char)
            elif char.isalpha():
                cur_str += char
            elif char == "[":
                stack.append((cur_str, k))
                k = 0
                cur_str = ""
            elif char == "]":
                last_char, last_k = stack.pop(-1)
                cur_str = last_char + last_k * cur_str
        return cur_str
