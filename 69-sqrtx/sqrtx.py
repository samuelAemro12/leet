class Solution:
    def mySqrt(self, x):
        if x < 0:
            return 0
        if x == 0:
            return 0
        low = 0
        high = x
        answer = 0

        while low <= high:
            mid = low + (high - low) // 2
            mid_squared = mid * mid
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

solution = Solution()

print(f"Sqrt(4) = {solution.mySqrt(4)}")
print(f"Sqrt(8) = {solution.mySqrt(8)}")
print(f"Sqrt(0) = {solution.mySqrt(0)}")
print(f"Sqrt(1) = {solution.mySqrt(1)}")
print(f"Sqrt(2147395599) = {solution.mySqrt(2147395599)}")
