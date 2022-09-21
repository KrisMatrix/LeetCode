class Solution:
    def mySqrt(self, x: int) -> int:
        # Since they want to only find the integral part of the 
        # square root, we can apply the "Repeated Subtraction 
        # Method of Square Root"
        # This is a very simple method. We subtract the consecutive 
        # odd numbers from the number for which we are finding the 
        # square root, till we reach 0 or the next odd number is 
        # greater than what is remaining. 

        # Let's try 16 which has a sqrt of 4
        # 16 - 1 = 15
        # 15 - 3 =12
        # 12 - 5 = 7
        # 7- 7 = 0
        # You can observe that we have subtracted 4 times. Thus,√16 = 4
        
        # Let's try 8 which has a sqrt of 4
        # 8 - 1 = 7
        # 7 - 3 = 4
        # 4 <  5, therefore sqrt is 2.
        
        odd_no = 1
        count = 0
        while (odd_no <= x):
            x = x - odd_no
            count += 1
            odd_no += 2
            
        return count

