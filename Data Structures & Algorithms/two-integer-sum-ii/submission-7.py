class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, i_value in enumerate(numbers):
#            print(f"i: {i}, {i_value}")
            # initial config
            pos_i, pos_f = i+1, len(numbers)
            counter_limit = pos_f - pos_i + 1
            counter = 0
            while True:
                counter += 1
                if counter == counter_limit:
                    break
 #               print(f"While pos_i, pos_f: {pos_i}, {pos_f}")
                if pos_i == pos_f:
                    break
                delta = int((pos_f-pos_i)/2)
  #              print(f"delta: {delta}")
                j = pos_i + delta
                j_value = numbers[j]
   #             print(f"values tested (i,j): {i_value}, {j_value}")
                if i_value + j_value == target:
                    return [i+1, j+1]
                elif i_value + j_value < target:
                    pos_i = j
                else: # i_value + j_value > target:
                    pos_f = j
                if delta == 0:
                    break

            #for j, j_value in enumerate(numbers[i+1:]):
             #   if i_value + j_value == target:
              #      return [i+1,i+j+2]