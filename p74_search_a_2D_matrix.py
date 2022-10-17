class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.target = target
        self.matrix = matrix
        return self.return_node(0,0)
    
    def return_node(self, row, col):
        if self.matrix[row][col] == self.target:
            return True
        elif self.matrix[row][col] == None:
            return False
        
        right = False
        down = False
        
        if ((col+1) < len(self.matrix[0])) and ((row+1) < len(self.matrix)):
            print(row,col)
            if self.matrix[row+1][col] <= self.target:
                return self.return_node(row+1, col)
            elif self.matrix[row][col+1] <= self.target:
                return self.return_node(row, col+1)
        
        if (col + 1) < len(self.matrix[0]):
            if self.matrix[row][col+1] <= self.target:
                right = self.return_node(row, col+1)
        if (row + 1) < len(self.matrix):
            if self.matrix[row+1][col] <= self.target:
                down = self.return_node(row+1, col)
        
        return right or down
