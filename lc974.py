class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        res = 0
        mpp = {0 : 1}
        sums = [0] * (len(nums) + 1)
        for x in range(0, len(nums)):
            sums[x + 1] = sums[x] + nums[x]

            rem = sums[x + 1] % k 
            
            res += mpp.get(rem, 0)

            mpp[rem] = mpp.get(rem, 0) + 1

        print(nums)
        print(sums)
        return res



x = Solution()
print(x.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))
        
