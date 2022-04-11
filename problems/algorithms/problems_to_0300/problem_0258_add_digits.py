class Solution:
    def addDigits(self, num: int) -> int:
        answer = str(num)
        while len(answer) > 1:
            newAnswer = 0
            for s in str(answer):
                newAnswer += int(s)
            answer = str(newAnswer)
        return int(answer)
