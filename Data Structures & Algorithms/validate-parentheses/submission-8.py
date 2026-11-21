class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        replace = {"(":")", "{":"}", "[":"]"}
        for subs in s:
            if subs in replace.keys():
                stack.append(subs)
            else:
                if not stack:
                    return False
                elif replace[stack[-1]] != subs:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        else:
            return True
        