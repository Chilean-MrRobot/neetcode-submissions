class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        top_candiate, delta = 0, 2**16 - 1
        counter = 0
        while left <= right:

            mid = left + (right - left) // 2
            print(f"{mid} {left} {right}")
            delta_i = x - mid*mid
            
            if delta_i == 0:
                return mid
            elif delta_i < 0: # mid*mid too big
                right = mid - 1
            else: # delta_i > 0, mid*mid too small
                left = mid + 1
                
            if abs(delta_i) < abs(delta):
                delta = delta_i
                top_candidate = mid

        return left - 1