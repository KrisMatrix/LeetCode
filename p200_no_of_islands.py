class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.no_of_islands = 0
        self.grid = grid
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col] == "1":
                    self.check_neighbours(row,col)
                    self.no_of_islands += 1
        return self.no_of_islands
    
    def check_neighbours(self,row,col):
        if (row < 0) or (col < 0) or (row >= len(self.grid)) or (col >= len(self.grid[0])):
            return
        if self.grid[row][col] == "2": # means already visited
            return
        if self.grid[row][col] == "1":
            self.grid[row][col] = "2"
            self.check_neighbours(row+1,col)
            self.check_neighbours(row-1,col)
            self.check_neighbours(row,col+1)
            self.check_neighbours(row,col-1)
