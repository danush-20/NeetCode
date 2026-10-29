class Solution:
    def maxArea(self, height: list[int]) -> int:
        l , r = 0 , len(height)-1
        maxarea = 0
        while l <= r:
            h = min(height[l],height[r])
            w = r - l
            area = h*w

            maxarea = max(maxarea,area)

            if height[l] == h:
                l+=1
            elif height[r] == h:
                r-=1
        return maxarea
            
            
        