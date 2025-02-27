class Solution(object):
    def plusOne(self, myArray):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(myArray) - 1, -1, -1):
            if myArray[i] < 9:
                myArray[i] += 1
                return myArray
            myArray[i] = 0
        return [1] + myArray
solution = Solution()
result = solution.plusOne([1, 2, 3, 6, 7, 8])
print(result)
