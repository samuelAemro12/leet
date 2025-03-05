class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        longest = 0
        dp = {}

        for j in range(n):
            for k in range(j):
                required = arr[j] - arr[k]
                i = index.get(required)
                if i is not None and i < k:
                    dp[(k, j)] = dp.get((i, k), 2) + 1
                    longest = max(longest, dp[(k, j)])
        return longest if longest >= 3 else 0
solution = Solution()
arr = [2,4,5,6,8,8]
result = solution.lenLongestFibSubseq(arr)
print(result)
