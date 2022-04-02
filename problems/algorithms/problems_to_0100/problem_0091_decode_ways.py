
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def process(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = process(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                res += process(i + 2)
            dp[i] = res
            return res
        return process(0)

    # slow decision
    def numDecodings2(self, s: str) -> int:
        if s[0] == "0":
            return 0

        def process(position, current_count):
            if len(s) == position:
                current_count += 1
                return current_count

            for i in range(0, 2, 1):
                if int(s[position:position + i + 1]) in range(1, 27) and position + i + 1 <= len(s):
                    current_count = process(position + i + 1, current_count)
                else:
                    return current_count
            return current_count

        count = process(0, 0)
        return count

