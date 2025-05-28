class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k == 0:
            return 0

        res = l = 0
        product = 1
        for r in range(0, len(nums)):
            product *= nums[r] 

            while product >= k and l <= r:
                res += len(nums) - r  
                product /= nums[l]
                l += 1
                


        return len(nums) * (len(nums) + 1) // 2 - res


x = Solution()
#print(x.numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))


print(x.numSubarrayProductLessThanK(nums = [1,1,1], k = 1))
