class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            last = nums.pop()
            nums.insert(0, last)
    
    def rotate_1(self, nums: List[int], k: int) -> None:
        for i in range(k):
            j = len(nums) - 1
            while j != 0:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
