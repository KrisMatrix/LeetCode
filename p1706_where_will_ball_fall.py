class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        self.grid = grid
        no_of_balls = len(self.grid[0])
        print(no_of_balls)
        retVal = []
        #for i in range(0,no_of_balls):
            #print("ball = "+ str(i))
        #    retVal.append(self.go_next(0, i))
        #return retVal
        #print("result="+str(self.go_next(0,0)))
        print("result="+str(self.go_next(0,1)))
        #print("result="+str(self.go_next(0,2)))
        #print("result="+str(self.go_next(0,3)))
        #print("result="+str(self.go_next(0,0)))
        
    def go_next(self, row, col):
        print("Called",row,col)
        if row == (len(self.grid)):
            print("1:",row,col)
            return col
        if self.grid[row][col] == 1:    #slope goes right
            if self.grid[row][col+1] == -1:
                print("2:",row,col)
                #return False
                return -1
            if col >= len(self.grid[row]):  #If you current column is a right edge
                print("3:",row,col)
                #stop
                return -1
                #break
            if self.grid[row][col+1] == -1: #opposing column
                print("4:",row,col)
                return -1
            print("5:",row,col)
            return self.go_next(row+1, col+1)  # go diagonal right
        if self.grid[row][col] == -1:    #slope goes left
            if self.grid[row][col-1] == +1:
                print("6:",row,col)
                return -1
            if col <= 0:  #If you current column is a left edge
                #stop
                print("7:",row,col)
                return -1
                #break
            if self.grid[row][col-1] == +1: #opposing column
                print("8:",row,col)
                return -1
            print("9:",row,col)
            return self.go_next(row+1, col-1)  # go diagonal left
