class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
 #           print(f"{left} {s[left]} {right} {s[right]}")
            if (not s[left].isalnum()) or (s[left] == " "):
                left += 1
                continue
            if (not s[right].isalnum()) or (s[right] == " "):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True