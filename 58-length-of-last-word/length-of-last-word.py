class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        output = s.strip()
        outputA = output.split(' ')
        return len(outputA[-1]) if outputA else 0
        
Solution_instance= Solution()
cin = "I am emperor"
x = Solution_instance.lengthOfLastWord(cin)
print(x)