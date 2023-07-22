from typing import List


# T: O(m * log(n))
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:
            l, r = 0, len(row) - 1

            while l <= r:
                m = (l + r) // 2
                if row[m] < 0:
                    r = m - 1
                else:
                    l = m + 1

            count += (len(row) - l)
        return count


# T: O(n+m)
class Solution2:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0

        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if grid[row][col] < 0:
                count += rows - row
                col -= 1
            else:
                row += 1
        return count