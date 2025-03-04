class Solution:
    def checkPowersOfThree(self, number: int) -> bool:
        while number > 0:
            if number % 3 > 1:
                return False
            number //= 3
        return True  
solution = Solution()
number = 45
result = solution.checkPowersOfThree(number)
print(result) 
