class Solution:
    def myAtoi(self, s: str) -> int:
        retval = 0
        state = 0
        sign = 1
        for i in s:
            if state == 0:
                if i == " ":             #leading spaces
                    continue    
                elif i == "-":
                    sign = -1
                    state = 1
                elif i == "+":
                    sign = 1
                    state = 1
                elif ord(i) >= 48 and ord(i) <= 57:
                    retval = retval * 10 + ord(i) - 48
                    state = 1
                else:
                    break
            else:
                if ord(i) >= 48 and ord(i) <= 57:
                    retval = retval * 10 + ord(i) - 48
                else:
                    break
            
        retval = retval * sign
        if (retval > 2**31 - 1):
            retval = 2**31 - 1
        elif retval < (-2**31):
            retval = -2**31
        return retval
