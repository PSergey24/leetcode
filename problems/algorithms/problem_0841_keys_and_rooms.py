from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        seen_rooms = set(stack)

        while stack:
            idx = stack.pop()

            for j in rooms[idx]:
                if j not in seen_rooms:
                    stack.append(j)
                    seen_rooms.add(j)

        return len(seen_rooms) == len(rooms)
