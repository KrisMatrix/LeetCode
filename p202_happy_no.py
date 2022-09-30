class Solution:
    def isHappy(self, n: int) -> bool:
        hash = {}
        while n != 1:
            if n in hash.keys():
                n = 0
                break
            hash[n] = 1
            n = self.summation(n)
        return n
            
    def summation(self, n):
        retval = 0
        while(n >= 10):
            retval += (n % 10 ) ** 2
            n = n // 10
        return retval + n*n
