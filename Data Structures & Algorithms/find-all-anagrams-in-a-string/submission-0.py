class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_table = {}
        len_p = len(p)
        for value in p:
            if value not in p_table.keys():
                p_table[value] = 1
            else:
                p_table[value] += 1
        s_table = {}
        i = 0
        return_list = []
        for j, value in enumerate(s):
            # Add
            if value not in s_table.keys():
                s_table[value] = 1
            else:
                s_table[value] += 1
            # Delete
            if j >= len_p:
                if s_table[s[i]] == 1:
                    del s_table[s[i]]
                else:
                    s_table[s[i]] -= 1
                i += 1
            # Compara
            if s_table == p_table:
                return_list.append(i)
        return return_list

