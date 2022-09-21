class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 1. start with last index
        # 2. add one.
        # 3. if number is >= 10, subtract 10, and set carry to 1
        # 4. Move to next digit add carry
        # 5. Loop
        # 6. if carry at the end is 1, add 1 to first item.
        carry = 1
        for i in reversed(range(len(digits))):
            digits[i] = digits[i] + carry
            if digits[i] >= 10:
                digits[i] -= 10
                carry = 1
            else:
                carry = 0
                break
        if carry == 1:
            digits.insert(0,1)
        return digits
                
