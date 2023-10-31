
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        pointer_s = 0
        pointer_t = 0

        for i in range(pointer_s, len(s), 1):
            for j in range(pointer_t, len(t), 1):
                if s[i] == t[j]:
                    pointer_t = j + 1
                    break
            else:
                return False
        else:
            return True
