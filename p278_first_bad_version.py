# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
      return self.binary_search(1, n)
    
    def binary_search(self, start, end):
      mid = int((start +end)/2)
      if (isBadVersion(mid) == True) and (start == end):
        return mid
      elif isBadVersion(mid) == False:
        return self.binary_search(mid + 1, end)
      else:
        return self.binary_search(start, mid)
