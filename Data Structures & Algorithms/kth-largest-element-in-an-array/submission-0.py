import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for i in range(len(nums)-k):
            _ = heapq.heappop(nums) # retiramos len-k menores valores
        return nums[0]