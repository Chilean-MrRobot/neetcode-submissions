class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_list = []
        plus_one = True
        digits.reverse()
        for i, value in enumerate(digits):
            if value == 9 and plus_one and i+1 == len(digits):
                new_list.append(0)
                new_list.append(1)
            elif value == 9 and plus_one:
                new_list.append(0)
            elif plus_one:
                new_list.append(value+1)
                plus_one = False
            else:
                new_list.append(value)
        new_list.reverse()
        return new_list
