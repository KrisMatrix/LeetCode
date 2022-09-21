class Solution:
  def runningSum1(self, nums: List[int]) -> List[int]:
    runningSum = []
    runningSum.append(nums[0])
    for i in range(1,len(nums)):
      last = runningSum.pop()
      runningSum.append(last)
      runningSum.append(last + nums[i])
    return runningSum
  
  def runningSum(self, nums: List[int]) -> List[int]:
    runningSum = [nums[0]] * len(nums)
    #runningSum.append(nums[0])
    for i in range(1,len(nums)):
      runningSum[i] = runningSum[i-1] + nums[i]
    return runningSum
    
