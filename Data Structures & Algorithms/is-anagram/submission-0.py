class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s, freq_t = {}, {}
        for i in s:
            if i in freq_s.keys():
                freq_s[i] += 1
            else:
                freq_s[i] = 1
        for i in t:
            if i in freq_t.keys():
                freq_t[i] += 1
            else:
                freq_t[i] = 1
        if sorted(freq_s.items()) == sorted(freq_t.items()):
            return True
        else:
            return False
        