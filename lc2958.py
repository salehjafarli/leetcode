class Solution:
    def maxSubarrayLength(self, nums, k: int) -> int:
        mpp = {}
        l = res = 0 
        for r in range(0, len(nums)):
            mpp[nums[r]] = mpp.get(nums[r], 0) + 1

            while mpp.get(nums[r], 0) > k:
                mpp[nums[l]] -= 1
                l += 1


            res = max(res, r - l + 1)

            
        return res



x = Solution()
print(x.maxSubarrayLength(nums = [1,2,3,1,2,3,1,2], k = 2))




        
