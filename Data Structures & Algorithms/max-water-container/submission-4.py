class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lb_pos = 0
        rb_pos = len(heights) - 1
        volume = 0
        while lb_pos != rb_pos:
#            print(f"{lb_pos} - {rb_pos}")
            volume_it = (rb_pos - lb_pos)*min(heights[lb_pos], heights[rb_pos])
            if volume_it > volume:
                volume = volume_it
            if heights[lb_pos] <= heights[rb_pos]:
                lb_pos += 1
            else: 
                rb_pos -= 1
        return volume
        