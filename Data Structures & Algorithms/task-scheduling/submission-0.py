class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict_freqs = {}
        for letter in tasks:
            if letter in dict_freqs.keys():
                dict_freqs[letter] += 1
            else: #new letter
                dict_freqs[letter] = 1
        print(dict_freqs)
        sorted_values = sorted(dict_freqs.values(), reverse=True)
        print(sorted_values)
        max_value = sorted_values[0]
        max_value_freq = 0
        for value in sorted_values:
            if value == max_value:
                max_value_freq += 1
            else:
                break
        print(f"mv: {max_value}, {max_value_freq}")
        del sorted_values[:max_value_freq]
        # Calculations
        lenght_candidate = (max_value-1)*(n+1) + max_value_freq
        capacity = lenght_candidate - max_value*max_value_freq
        total_sum_rest = sum(sorted_values)
        print(f"{lenght_candidate}, {capacity}, {total_sum_rest}")
        if total_sum_rest > capacity:
            return lenght_candidate + total_sum_rest - capacity
        else:
            return lenght_candidate

