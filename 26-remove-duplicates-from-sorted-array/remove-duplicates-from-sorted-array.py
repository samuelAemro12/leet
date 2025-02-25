from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_index] = nums[i]  
                unique_index += 1 
        return unique_index

nums = [1, 2, 3, 4, 5, 6, 7, 7, 7, 8, 8, 9]
solution = Solution()
length = solution.removeDuplicates(nums)
print(length) 
print(nums[:length])