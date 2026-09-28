"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_rooms = 0
        counter_rooms = 0
        ends = []
        heapq.heapify(ends)

        intervals_sorted = sorted(intervals, key=lambda x: x.start)

        for interval in intervals_sorted:
            counter_rooms += 1
            heapq.heappush(ends, interval.end)
            while interval.start >= ends[0]:
                heapq.heappop(ends)
                counter_rooms -= 1
            max_rooms = max(max_rooms, counter_rooms)
        return max_rooms
            
