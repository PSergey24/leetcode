from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort()
        prev = points[0]
        total = 1

        for l, r in points[1:]:
            if l > prev[1]:
                total += 1
                prev = [l, r]
            else:
                prev[1] = min(prev[1], r)
        return total
