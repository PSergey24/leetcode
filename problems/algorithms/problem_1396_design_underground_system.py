from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        self.i = defaultdict(tuple)
        self.o = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.i[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time, start_station = self.i[id]
        total = t-start_time
        self.o[(start_station, stationName)].append(total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.o[(startStation, endStation)])/len(self.o[(startStation, endStation)])
