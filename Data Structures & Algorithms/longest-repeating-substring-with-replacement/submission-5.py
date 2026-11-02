class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_lenght = 0
        i=0
        hash_table = {}

        for j, sj in enumerate(s):
            hash_table[sj] = hash_table.get(sj, 0) + 1
            while sum(hash_table.values()) - max(hash_table.values()) > k:
                hash_table[s[i]] -= 1
                i += 1
            max_lenght = max(max_lenght, sum(hash_table.values()))

        return max_lenght
            