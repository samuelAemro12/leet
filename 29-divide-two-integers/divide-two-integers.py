class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 0:
            raise ValueError("Cannot divide by zero.")
        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1 
        negative = (dividend < 0) ^ (divisor < 0)
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        quotient = abs_dividend // abs_divisor
        if negative:
            quotient = -quotient
        
        return quotient

solution = Solution()
try:
    output = solution.divide(24, 0)
    print(output)
except ValueError as e:
    print(e)  
output = solution.divide(24, 3)
print(output)  