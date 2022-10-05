class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.convert_string_to_int(num1) * self.convert_string_to_int(num2))
        
    def convert_string_to_int(self, num):
        hash = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 0
        }
        retval = 0
        for i in range(len(num)):
            retval = 10 * retval + hash[num[i]]
        return retval