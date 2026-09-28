class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        return_intervals = []
        candidate = newInterval # This size or bigger
        flag_candidate_appended = False

        for interval in intervals:
            if interval[1] < newInterval[0]: # before intersection
                return_intervals.append(interval)
            elif interval[0] > newInterval[1]: # after intersection
                if not flag_candidate_appended:
                    return_intervals.append(candidate)
                    flag_candidate_appended = True # only happens once
                return_intervals.append(interval)
            else: # all intersection scenarios
                candidate[0] = min(candidate[0], interval[0])
                candidate[1] = max(candidate[1], interval[1])
        
        if not flag_candidate_appended:
            return_intervals.append(candidate)
        
        return return_intervals
        