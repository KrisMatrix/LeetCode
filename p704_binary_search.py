class Solution:
    def binary_search(self, nums, start, end, target):
      if start == end and target != nums[start]:
        return -1
      mid = int((start + end)/2)
      if target < nums[mid]:
        return self.binary_search(nums, start, mid, target)
      elif target > nums[mid]:
        return self.binary_search(nums, mid+1, end, target)
      else:
        return mid
      
    def search(self, nums: List[int], target: int) -> int:
      return self.binary_search(nums, 0, len(nums)-1, target)
