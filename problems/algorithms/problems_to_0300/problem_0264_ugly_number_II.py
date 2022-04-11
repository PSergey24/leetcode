
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_num_list = [1]

        two_pos = 0
        three_pos = 0
        five_pos = 0

        while len(ugly_num_list) < n:
            by2 = ugly_num_list[two_pos] * 2
            by3 = ugly_num_list[three_pos] * 3
            by5 = ugly_num_list[five_pos] * 5

            minimum = min(by2, by3, by5)
            ugly_num_list.append(minimum)

            if minimum == by2:
                two_pos += 1
            if minimum == by3:
                three_pos += 1
            if minimum == by5:
                five_pos += 1
        return ugly_num_list[-1]
