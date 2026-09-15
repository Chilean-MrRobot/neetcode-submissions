class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_strings = {}
        sorted_anas = []

        for i, string in enumerate(strs):
            sorted_string = "".join(sorted(string))
            if sorted_string in hash_strings.keys():
                hash_strings[sorted_string].append(string)
            else: #value don't exists (yet)
                hash_strings[sorted_string] = [string]

        return [value for value in hash_strings.values()]