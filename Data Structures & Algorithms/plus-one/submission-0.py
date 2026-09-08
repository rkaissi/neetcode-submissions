class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        carry = 0
        one = 1
        for i in range(n-1, -1, -1):
            digits[i] = digits[i] + one + carry
            carry = digits[i] // 10
            digits[i] %= 10
            one = 0
        
        if carry:
            digits.insert(0, carry)
        
        return digits

            