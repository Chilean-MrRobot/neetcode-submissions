class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        len_s = len(s)
        r = 1
        views = set()

        if len_s == 1:
            return 1

        for l in range(len(s)-1):
#            print(f"s:{s[l:r]} ,l:{l} ,r:{r}")
            while r <= len_s and s[r-1] not in views:
            #while len(s[l:r]) == len(set(s[l:r])) and r <= len_s:
 #               print(f"while s:{s[l:r]} ,l:{l} ,r:{r}")
                longest = max(longest, r-l)
  #              print(f"{longest}")
                views.add(s[r-1])
                r += 1

            views.remove(s[l])

        return longest
