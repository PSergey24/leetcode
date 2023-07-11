from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = [[0] * cols for r in range(rows + 1)]

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if c > 0 and c < (cols - 1):
                    res[r][c] = matrix[r][c] + min(res[r+1][c-1], res[r+1][c], res[r+1][c+1])
                elif cols == 1:
                    res[r][c] = matrix[r][c] + res[r+1][c]
                elif c == 0:
                    res[r][c] = matrix[r][c] + min(res[r+1][c], res[r+1][c+1])
                elif c == (cols - 1):
                    res[r][c] = matrix[r][c] + min(res[r+1][c-1], res[r+1][c])

        return min(res[0])
