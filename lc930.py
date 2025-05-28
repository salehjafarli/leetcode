class Solution:
    def numSubarraysWithSum(self, nums, goal: int) -> int:
        res = 0
        mpp = {0 : 1}
        sums = [0] * (len(nums) + 1)
        for x in range(0, len(nums)):
            sums[x + 1] = sums[x] + nums[x]

            remainder = sums[x + 1] - goal
            
            rmcnt = mpp.get(remainder)
            if rmcnt is not None:
                res += rmcnt


            mpp[sums[x + 1]] = mpp.get(sums[x + 1], 0) + 1

        return res





x = Solution()
#print(x.numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))


print(x.numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0))
