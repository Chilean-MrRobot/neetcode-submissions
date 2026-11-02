class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_string = ""
        counter_pos = 0
        flag = False
        while counter_pos < len(strs[0]):
            char = strs[0][counter_pos]
            for str_i in strs:
                if len(str_i) <= counter_pos:
                    flag = True
                    break
                if str_i[counter_pos] != char:
                    flag = True
                    break
            if flag:
                break
            longest_string += char
            counter_pos += 1
        return longest_string
