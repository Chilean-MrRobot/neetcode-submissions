class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:len(s1)])
        if s1_counts == window_counts:
            return True
        for i in range(len(s1), len(s2)):
            start_char = s2[i - len(s1)]
            new_char = s2[i]
            window_counts[new_char] += 1
            window_counts[start_char] -= 1
            if window_counts[start_char] == 0:
                del window_counts[start_char]
            if s1_counts == window_counts:
                return True
        return False