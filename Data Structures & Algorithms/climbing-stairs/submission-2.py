class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        else:
            return self.climbStairs(n-3) + 2*self.climbStairs(n-2)