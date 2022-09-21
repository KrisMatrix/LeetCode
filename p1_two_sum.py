class Solution:
    def twoSum_brute(self, nums: List[int], target: int) -> List[int]:
        # O(n^2)
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    print("i =",i)
                    print("j =",j)
                    print("i value =",nums[i])
                    print("j value =",nums[j])
                    answer.append(i)
                    answer.append(j)
                    break
        print("done")
        return answer
      
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #O(n)
      hash = {}
      for i in range(len(nums)):
        if nums[i] in hash:
          return hash[nums[i]], i
        hash[target - nums[i]] = i
