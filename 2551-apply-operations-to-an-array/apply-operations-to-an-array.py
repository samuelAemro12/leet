class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1] and nums[i] != 0:
                nums[i] *= 2  
                nums[i + 1] = 0  
        result = []
        for num in nums:
            if num != 0:
                result.append(num)
        result.extend([0] * (n - len(result)))
        
        return result


solution = Solution()
nums = [2, 2, 0, 4, 4]
result = solution.applyOperations(nums)
print(result) 