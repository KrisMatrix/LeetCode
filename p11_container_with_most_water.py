class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_ptr = 0
        r_ptr = len(height) - 1
        maxVal = 0
        while (l_ptr < r_ptr):
            if ((r_ptr - l_ptr) * min(height[l_ptr], height[r_ptr])) > maxVal:
                maxVal = (r_ptr - l_ptr) * min(height[l_ptr], height[r_ptr])
            if height[l_ptr] >= height[r_ptr]:
                r_ptr -= 1
            else:
                l_ptr += 1
        return maxVal

obj = Solution()
print(obj.maxArea([1,8,6,2,5,4,8,3,7]))
print(obj.maxArea([1,1]))
