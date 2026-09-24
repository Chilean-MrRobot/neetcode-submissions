import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        len_nums = len(nums)
        heapq.heapify(nums)
        if len_nums > k:
            for i in range(int(len_nums-k)):
                _ = heapq.heappop(nums)
        self.nums = nums # heap with len k

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)  # First push new value
        if len(self.nums) > self.k:
            backup_val = heapq.heappop(self.nums) # Then pop the lower one
        if len(self.nums) > 0:
            return self.nums[0]
        return backup_val