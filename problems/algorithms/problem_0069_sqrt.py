

class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x

        l, r = 1, x

        while l <= r:
            middle = l + (r - l) // 2

            if middle * middle > x:
                r = middle - 1
            elif middle * middle < x:
                l = middle + 1
            else:
                return middle
        else:
            return r
