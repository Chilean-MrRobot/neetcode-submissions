class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1:
            return True
        else:
            values = [n]
            str_value = str(n)
            while True:
                sum = 0
                for value in str_value:
                    sum += int(value)*int(value)
                if sum == 1:
                    return True
                elif sum in values:
                    return False
                else:
                    values.append(sum)
                    str_value = str(sum)
