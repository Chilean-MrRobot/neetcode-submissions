class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        ordered_intervals = sorted(intervals, key=lambda x: x[1])
        counter_overlaped_out = 0
        end = ordered_intervals[0][1]

        for interval in ordered_intervals[1:]:
            if end > interval[0]:
                counter_overlaped_out += 1
            else: #todo ok
                end = interval[1]

        return counter_overlaped_out