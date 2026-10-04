class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_set = set()
        j = 0
        counter = 0

        for i in range(len(s)):
            if j == len(s):
                break

            while j < len(s) and s[j] not in hash_set:
                hash_set.add(s[j])
                j += 1

            hash_set.remove(s[i])
            counter = max(counter, j-i)

        return counter