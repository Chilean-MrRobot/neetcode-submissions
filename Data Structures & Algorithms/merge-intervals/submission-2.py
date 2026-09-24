class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals_ordered = sorted(intervals, key=lambda x: x[0])

        intervals_overlap = [] # return list
        candidate = intervals_ordered[0] # first interval

        for i in range(len(intervals_ordered) - 1):
            if candidate[1] >= intervals_ordered[i+1][0]: # comparing end to start
                if intervals_ordered[i+1][1] > candidate[1]:
                    candidate[1] = intervals_ordered[i+1][1] # expand ending of candidat
            else: # No overlap
                intervals_overlap.append(candidate)
                candidate = intervals_ordered[i+1]

        intervals_overlap.append(candidate)
        return intervals_overlap