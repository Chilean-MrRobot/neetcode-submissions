class Solution:
    def isValid(self, s: str) -> bool:
        chop_id = int(len(s)/2)
        print(chop_id)
        for i in range(chop_id):
            if s == "":
                return True
            if "()" in s:
                s = s.replace("()", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            else:
                return False
        if s == "":
            return True
        else:
            return False
        