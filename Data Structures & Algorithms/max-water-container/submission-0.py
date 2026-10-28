class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights)-1

        while left < right: 
            curr_area = min(heights[left],heights[right])*(right-left)
            max_area = max(max_area, curr_area)

            if heights[right] > heights[left]:
                left +=1 
            else:
                right -=1 
        
        return max_area