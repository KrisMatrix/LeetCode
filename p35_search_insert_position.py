class Solution:    
    def searchInsert(self, nums: List[int], target: int) -> int:
        # We are going to apply a binary search algorithm.
        # That will be O(log n)
        # if odd, go to mid point.
        # if even, go floor of mid point
        # if target value is < mid point, then go to lesser mid point of midpoint.
        # if target value is > midpoint, then go to greater mid point of midpoint.
        def searchA(nums, start, end, target) ->int:
            if start == end and target < nums[len(nums) - 1]:
                return start
            elif start == end and target > nums[len(nums) - 1]:
                return start + 1
            midpoint = floor((end+start)/2)
            #print(nums, start, end, target, midpoint)
            if target == nums[midpoint]:
                return midpoint
            elif target < nums[midpoint]:
                end = midpoint
                return searchA(nums, start, end, target)
            else:
                start = midpoint+1
                return searchA(nums, start, end, target)    
                
        retval = searchA(nums, 0, len(nums) - 1, target)
        #print("retval = "+str(retval))
        return retval
        
