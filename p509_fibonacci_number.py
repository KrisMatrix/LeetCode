class Solution:
    # following is a simple loop solution
    def fib_loop(self, n: int) -> int:
        f0 = 0
        f1 = 1
        i = 2
        #deal with edge cases
        if n == 0:
          f2 = f0
        elif n == 1:
          f2 = f1
          
        while i <= n:
          f2 = f0 + f1
          f0 = f1
          f1 = f2
          i += 1
        return f2
      
    
    # follwing is a recursive solution
    def fib_recursive(self, n: int) -> int:
      if n <= 1:
        return n
      return self.fib_recursive(n-1) +self.fib_recursive(n-2)
    
    #following is a dynamic solution
    memo = []
    for i in range(31):
      memo.append(-1)

    def fib(self, n: int) -> int:
      if n == 0:
        return 0
      if n == 1:
        return 1

      if self.memo[n] != -1:
        return self.memo[n]
    
      self.memo[n] = self.fib(n-1) + self.fib(n-2)
      return self.memo[n]
