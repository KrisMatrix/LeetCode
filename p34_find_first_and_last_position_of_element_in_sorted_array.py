class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      retval = [-1, -1]
      start = 0
      end = len(nums) - 1
      while(start < len(nums) and end >= 0):
        # the condition merely  checks for situations where 
        # target is much smaller or larger than any element in 
        # nums
        if nums[start] == target and nums[end] == target:
          retval = [start, end]
          break
        if nums[start] < target:
          start += 1
        elif nums[start] > target:
          break
        if nums[end] > target:
          end -= 1
        elif nums[end] < target:
          break
      return retval
      # This solution appears to be a O(n) solution.
