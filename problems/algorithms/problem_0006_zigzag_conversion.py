class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        start_step = numRows*2 - 2
        answer = ''
        for i in range(0, numRows, 1):
            step = self.change_step(start_step, i*2)

            j = i
            while j < len(s):
                answer += s[j]
                j += step
                step = self.change_step(start_step, step)
                if len(answer) == len(s):
                    break
        return answer

    def change_step(self, start_step, step):
        if start_step != step:
            return abs(start_step - step)
        else:
            return start_step