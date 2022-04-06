from typing import List
from collections import Counter


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        cnt = Counter(arr)
        ans = 0

        for i in cnt:
            for j in cnt:
                k = target - i - j
                if i == j == k:
                    ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2) // (3 * 2)
                elif i == j:
                    ans += cnt[i] * (cnt[i] - 1) // 2 * cnt[k]
                elif i < j < k:
                    ans += cnt[i] * cnt[j] * cnt[k]
        mod = 10**9+7
        return ans % mod
