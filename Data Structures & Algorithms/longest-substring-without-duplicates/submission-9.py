class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_lenght = 0
        i = 0
        freq_set = set()
        counter_freq = 0
        for j, sj in enumerate(s):
            if sj not in freq_set: 
                freq_set.add(sj)
                counter_freq += 1
                max_lenght = max(max_lenght, counter_freq)
            else:
                while sj in freq_set:
                    freq_set.remove(s[i])
                    counter_freq -= 1
                    i += 1
                freq_set.add(sj)
                counter_freq += 1
                max_lenght = max(max_lenght, counter_freq)
        return max_lenght