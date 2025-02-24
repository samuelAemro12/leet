class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        last = 0
        
        for char in s:
            currtVal = roman[char]  
            if currtVal > last:
                total += currtVal - 2 * last  
            else:
                total += currtVal  
            last = currtVal  

        return total
