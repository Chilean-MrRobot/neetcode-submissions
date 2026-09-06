class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, i_value in enumerate(prices):
            for j, j_value in enumerate(prices[i+1:]):
                if j_value - i_value > max_profit:
                    max_profit = j_value - i_value
        return max_profit
        