from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_table = {}
        for num in arr:
            hash_table[num] = hash_table.get(num, 0) + 1

        return len(set(hash_table.values())) == len(set(hash_table.keys()))
