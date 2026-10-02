class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start, current):
            subsets.append(current.copy())
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtracking(i+1, current)
                current.pop()
            return

        subsets = []
        backtracking(0, [])
        return subsets