class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks = []
        stackt = []
        for subs in s:
            if subs == "#" and stacks:
                stacks.pop()
            elif subs != "#":
                stacks.append(subs)
        for subt in t:
            if subt == "#" and stackt:
                stackt.pop()
            elif subt != "#":
                stackt.append(subt)
        if "".join(stacks) == "".join(stackt):
            return True
        else:
            return False