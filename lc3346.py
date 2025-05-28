class Solution:
    def maxFrequency(self, nums, k: int, numOperations: int) -> int:
        if len(nums) == 1:
            return 1

        nums.sort()
        
        res = l = m = 0
        for r in range(1, len(nums)):
            print(nums[l], nums[m], nums[r]) 
            if numOperations < 0:
                l += 1
                numOperations += 1
                while nums[m] - nums[l] <= k and m < r:
                    m += 1
                
            if nums[r] - nums[l] <= k:
                m = r 
                numOperations -= 1
            elif nums[r] - nums[m] <= k:
                numOperations -= 1
            else:
                while nums[r] - nums[l] > (2 * k):
                    l += 1
                    while m < r and nums[m] - nums[l] <= k:
                        m += 1

            res = max(res, r - l + 1)

        
        return res
            






x = Solution()
print(x.maxFrequency(nums = [5,11,20,20, 22, 22, 24, 27, 31, 32, 32], k = 5, numOperations = 10))


#print(x.maxFrequency(nums = [1,4,5], k = 1, numOperations = 2))


#print(x.maxFrequency(nums = [5,5,5], k = 1, numOperations = 0))


#print(x.maxFrequency(nums = [88, 53, 50], k = 27, numOperations = 2))





             

        
