import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        lowest_speed = right

        while left <= right:
            mid = left + (right-left)//2

            hours_total = 0
            for p in piles:
                hours_total += math.ceil(p/mid)

            if hours_total <= h:
                if mid < lowest_speed:
                    lowest_speed = mid
                right = mid - 1
            else: # Speed too slow
                left = mid + 1

        return lowest_speed
