class Solution:
    def repeatedCharacter(self, stringsVal: str) -> str:
        seen=set()
        for char in stringsVal:
            if char in seen:
                return char
            seen.add(char)
        return ""
stringsVal = "qwerewq"
solution = Solution()
result = solution.repeatedCharacter(stringsVal)  
print(result)