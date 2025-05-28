class Solution:
    def subarraySum(self, nums) -> int:
        res = 0
        sums = [0] * (len(nums) + 1)
        for i in range(0, len(nums)):
            sums[i + 1] = sums[i] + nums[i]

            start = max(0, i - nums[i])

            res += sums[i + 1] - sums[start]

        return res



x = Solution()
print(x.subarraySum(nums = [2,3,1]))


        
