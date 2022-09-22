class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
      stack = []
      
      #Even though there are two for loops, it is only O(n)
      for i in range(len(s)):
        if s[i] != '#':
          stack.append(s[i])
        else:
          if len(stack) > 0:
            stack.pop()
      
      s = stack
      stack = []
      
      for i in range(len(t)):
        if t[i] != '#':
          stack.append(t[i])
        else:
          if len(stack) > 0:
            stack.pop()
            
      t = stack

      if s == t:
        return True
      else:
        return False
      
