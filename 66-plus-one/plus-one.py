class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        j = len(digits) - 1
    
        while j >= 0:
            digits[j] += carry 
            carry = digits[j] // 10
            if carry < 1:
                break
            digits[j] = digits[j] % 10
            j -= 1   
        

        if carry > 0:
            digits.insert(0, 1)

        return (digits)