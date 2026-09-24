"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
        intervals_ordered = sorted(intervals, key=lambda x: x.start)
#        print(intervals_ordered[0].start)
        for i in range(len(intervals)-1):
            if intervals_ordered[i].end > intervals_ordered[i+1].start:
                return False
        return True
