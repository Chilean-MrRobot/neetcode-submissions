class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_cleaned = sorted(list(set(nums)))
        print(list_cleaned)
        print(sorted(nums))
        if list_cleaned == sorted(nums):
            return False
        return True
        