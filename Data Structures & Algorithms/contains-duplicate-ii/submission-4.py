class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        i, j = 0, k
        if len(set(nums[i:j+1])) < len(nums[i:j+1]):
            return True
        while j < len(nums):
 #           print(f"{i} {j} {nums[i:j+1]}")
            if nums[j] in nums[i:j]:
                return True
            j += 1
            i += 1
        return False

