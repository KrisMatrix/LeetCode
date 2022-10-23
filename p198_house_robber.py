class Solution:
    def rob_v1(self, nums: List[int]) -> int:
        # This is O(n) Time solution and O(n) Space
        memo = [0] * (len(nums)+3)
        for i in range(len(nums) - 1, -1, -1):
            memo[i] = nums[i] + max(memo[i+2], memo[i + 3])
        return max(memo[0], memo[1])
