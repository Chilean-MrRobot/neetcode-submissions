class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else: # target is on the right (unordered)
                    left = mid + 1
            else: # nums[mid] > target, right is ordered
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: # target is on the left (unordered)
                    right = mid - 1
        return -1