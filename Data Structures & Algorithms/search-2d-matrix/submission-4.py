class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix) - 1

        row = -1
        while up <= down:
            mid = up + (down - up)//2

            if matrix[mid][0] <= target:
                row = mid
                up = mid + 1
            else: # mid value too low
                down = mid - 1
        
        if row == -1:
            return False

        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left)//2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else: # too much to the right
                right = mid - 1

        return False