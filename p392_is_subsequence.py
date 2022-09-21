class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      i = 0
      for j in range(len(t)):
        if len(s) > 0 and i < len(s):
          if s[i] == t[j]:
            i += 1
          
      if i == len(s):
        return True
      else: 
        return False
