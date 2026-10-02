class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, current, suma):
            if suma == target:
                valid_combinations.append(current[:])
                return
            if suma > target:
                return

            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i, current, suma + nums[i])  # i, no i+1, porque se puede repetir
                current.pop()

        valid_combinations = []
        backtrack(0, [], 0)
        return valid_combinations