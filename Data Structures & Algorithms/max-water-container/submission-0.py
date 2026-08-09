class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        n = len(heights) 
        lo, hi = 0, n-1


        while lo < hi:
            water = min(heights[lo], heights[hi]) * (hi - lo)
            print(water)
            if max_water < water:
                max_water = water

            if heights[lo] < heights[hi]:
                lo += 1
            else:
                hi -= 1
        return max_water