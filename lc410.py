class Solution:
    def splitArray(self, nums, k: int) -> int:
        l = max(nums)
        h = sum(nums)
        res = float('inf')
        while l <= h:
            m = (l + h) // 2

            sub_res = sm = 0
            curr_k = k
            for i in range(len(nums)):
                sm += nums[i]
                if sm > m:
                    sm = nums[i]
                    curr_k -= 1 
                if curr_k == 0:
                    break
                sub_res = max(sm, sub_res)

            if curr_k == 0:
                l = m + 1
            else:
                res = sub_res
                h = m - 1

        return res

    def splitArray_dp(self, nums, k: int) -> int:
        #build dp(first col is reused as prefixsum)
        dp = [[float('inf')] * k for _ in range(len(nums))]
        dp[0][0] = nums[0]
        for i in range(1, len(nums)):
            dp[i][0] = dp[i - 1][0] + nums[i]

        #main
        for i in range(1, len(nums)):
            for j in range(1, min(i + 1, k)):
                mn = float('inf')
                for i2 in range(i - 1, j - 2, -1):
                    cut_sum = dp[i][0] - dp[i2][0]
                    cut_sum = max(dp[i2][j - 1], cut_sum)
                    mn = min(mn, cut_sum)
                dp[i][j] = mn
        
        return dp[-1][k - 1]


x = Solution()
print(x.splitArray([1, 2, 3, 4, 5], 1))

#print(x.splitArray_dp([7, 2, 5, 10, 8], 2))