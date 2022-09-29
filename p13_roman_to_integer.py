class Solution:
    def romanToInt(self, s: str) -> int:
        hash = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        prev = 0 
        result  = 0
        for i in reversed(s):
            if hash[i] < prev:
                result -= hash[i]    
            else:
                result += hash[i]
                prev = hash[i]
        return result
