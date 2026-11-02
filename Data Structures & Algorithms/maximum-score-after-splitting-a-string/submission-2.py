class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        left_score, right_score = 0, 0
        for i in s:
            if i == "1":
                right_score += 1
        for i in s[:-1]:
            if i == "0":
                left_score += 1
            else:
                right_score -= 1
            max_score = max(max_score, left_score + right_score)
        return max_score
        