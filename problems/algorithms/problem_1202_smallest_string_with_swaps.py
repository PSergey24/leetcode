from typing import List
from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        edge = defaultdict(list)
        for x, y in pairs:
            edge[x].append(y)
            edge[y].append(x)

        n = len(s)
        res = [""] * n
        visit = set()
        for i in range(n):
            if i in visit:
                continue
            q = [i]
            visit.add(i)

            char, pos = [], []
            while q:
                cur = q.pop()
                pos.append(cur)
                char.append(s[cur])

                for nei in edge[cur]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)

            char.sort()
            pos.sort()
            for p, c in zip(pos, char):
                res[p] = c
        return "".join(res)

