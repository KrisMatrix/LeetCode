class Solution:
    memo = {}
    def climbStairs(self, n: int) -> int:
        if n in self.memo.keys():
          return self.memo[n]
        elif n == 1:
          self.memo[n] = 1
          return 1  # one way to make n=1 step. i,e take a single step
        elif n == 2:
          self.memo[n] = 2
          return 2  # two ways to make 2 steps. i.e. take two single steps or take a double step
        else:
          if (n-1) not in self.memo.keys():
            self.memo[n-1] = self.climbStairs(n-1)
          if (n-2) not in self.memo.keys():
            self.memo[n-2] = self.climbStairs(n-2)
          return self.memo[n-1] + self.memo[n-2]
