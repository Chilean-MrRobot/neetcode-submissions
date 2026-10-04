"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_list = sorted(intervals, key=lambda x: x.start)
        print([(el.start, el.end) for el in sorted_list])
        for i, interval in enumerate(sorted_list):
            if i == len(intervals) - 1:
                continue
            print((interval.start, interval.end))
            if interval.start <= sorted_list[i+1].start < interval.end:
                return False

        return True