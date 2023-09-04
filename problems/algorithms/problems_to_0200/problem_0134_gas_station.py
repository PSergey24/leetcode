from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        tank = 0
        start_point = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += (g - c)
            if tank < 0:
                tank = 0
                start_point = i + 1

        if start_point < len(gas) + 1:
            return -1
        return start_point
