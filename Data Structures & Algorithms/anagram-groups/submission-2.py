def get_frequency(str: str) -> tuple:
    dict_s = {}
    for s in str:
        if s in dict_s.keys():
            dict_s[s] += 1
        else:
            dict_s[s] = 1
    return tuple(sorted(dict_s.items()))

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagrams = {}
        for str in strs:
            anagram = get_frequency(str)
            if anagram not in dict_anagrams:
                dict_anagrams[anagram] = []
            dict_anagrams[anagram].append(str)
        return list(dict_anagrams.values())