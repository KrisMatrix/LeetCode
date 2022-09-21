class Solution:
    def reverse(self, x: int) -> int:
      if (x < 0):
        pos_or_neg = -1
      else:
        pos_or_neg = 1
        
      y = 0
      x = abs(x)
      while x != 0:
        y = y * 10 + x % 10
        x = x // 10
        
      y = y * pos_or_neg
      if y >=0 and y > 2**31:
        y = 0
      elif y < 0 and y < -1*2**31 - 1:
        y = 0
      return y
