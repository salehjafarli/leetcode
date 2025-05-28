class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        l = res = 0        
        m = 1
        for r in range(2, len(nums)):
            if (nums[r] + nums[l]) * 2 == nums[m]:
                res += 1
            m += 1
            l += 1
        
        return res
