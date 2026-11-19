class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # First sort
        nums.sort(reverse=True)
        print(nums)
        # Binary Search
        left = 0
        right = len(nums)

        while left <= right:
            mid = left + (right - left) // 2
            print(f"left: {left} right: {right}")
            print(f"mid: {mid}")
            # calculate is mid is the special value
            counter = 0
            while counter < len(nums) and nums[counter] >= mid:
                counter += 1
            print(f"counter: {counter}")

            if counter == mid:
                return mid
            elif counter < mid:
                right = mid - 1
            else:
                left = mid + 1

        return -1