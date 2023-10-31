

class Solution:
    def reverseVowels(self, s: str) -> str:
        symbols = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        slist = list(s)

        l, r = 0, len(slist) - 1

        while l < r:
            if slist[r] not in symbols:
                r -= 1
                continue
            if slist[l] not in symbols:
                l += 1
                continue

            slist[l], slist[r] = slist[r], slist[l]
            r -= 1
            l += 1

        return "".join(slist)
