class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ''
        while columnNumber:
            current = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            res = chr(current + ord('A')) + res
        return res

