class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = left + (right - left) // 2

            if nums[mid] < nums[right]: # right sorted
                right = mid
            else: # left sorted
                left = mid + 1

        return nums[left]