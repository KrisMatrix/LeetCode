class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums)+1)
        
        for i in range(1,len(nums)+1):
          prefix[i] = prefix[i-1] + nums[i-1]

        for i in range(len(nums)):
          if prefix[i] == (prefix[len(prefix) - 1] - prefix[i] - nums[i]):
            return i
        
        return -1
