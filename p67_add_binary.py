class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        result = []
        carry = 0
        while(len(a) != 0 or len(b) != 0):
            if len(a) > 0:
                carry += int(a.pop())
            if len(b) > 0:
                carry += int(b.pop())
                
            if carry < 2:
                result.insert(0,str(carry))
                carry = 0
            elif carry == 2:
                result.insert(0,str(0))
                carry = 1
            elif carry == 3:
                result.insert(0,str(1))
                carry = 1
        if carry:
            result.insert(0,str(1))
        return ''.join(result)
