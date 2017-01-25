class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        length = len(height)
        area = [None]*(length*(length-1) / 2)
        count = 0
        for key_i, height_i in enumerate(height):
            for key_j in range(key_i+1,length):
                if height_i >= height[key_j]:
                    area[count] = (key_j - key_i)*height[key_j]
                    count += 1
                else:
                    area[count] = (key_j - key_i) * height_i
                    count += 1
        return max(area)
        """
        left, right = 0,len(height)-1
        max_area = 0
        area = 0
        while left < right:
            h_l, h_r = height[left], height[right]
            if h_l < h_r:
                area = (right - left)*h_l
                while height[left]<=h_l:
                    left += 1
            else:
                area = (right - left) * h_r
                while height[right] <= h_r:
                    right -= 1
            if area > max_area:
                max_area = area
        return max_area
sol = Solution()
print sol.maxArea([1,2,3,4,5])