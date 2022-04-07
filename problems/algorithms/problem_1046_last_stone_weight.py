from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []

        def push(x):
            heapq.heappush(h, -x)

        def pop():
            return -heapq.heappop(h)

        for x in stones:
            push(x)

        while len(h) > 1:
            x = pop()
            y = pop()

            if x != y:
                push(abs(x - y))

        if len(h) == 0:
            return 0
        return pop()
