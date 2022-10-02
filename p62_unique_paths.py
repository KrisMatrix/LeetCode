class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.m = m
        self.n = n
        self.hash = {}
        return self.solve(0, 0)
        
    def solve(self, row, col):
        if str(row)+"+"+str(col) in self.hash.keys():
            return self.hash[str(row)+"+"+str(col)]
        elif (row == self.m - 1) and (col == self.n - 1):
            self.hash[str(row)+"+"+str(col)] = 1
            return 1
        elif (row >= self.m) or (col >= self.n):
            self.hash[str(row)+"+"+str(col)] = 0
            return 0
        else:
            self.hash[str(row)+"+"+str(col)] = self.solve(row, col + 1) + self.solve(row + 1, col)
            return self.hash[str(row)+"+"+str(col)]
