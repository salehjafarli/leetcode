class Solution:
    def minimumSubarrayLength(self, nums, k: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] >= k else -1

        res = 99999
        for i in range(0, len(nums)):
            ors = 0
            for j in range(i, len(nums)):
                if j - i + 1 >= res:
                    break
                
                ors |= nums[j]
                if ors >= k:
                    res = min(res, j - i + 1)

                    if res == 1:
                        return 1
                    break



        return -1 if res == 99999 else res



x = Solution()
print(x.minimumSubarrayLength(nums = [2, 1, 1, 22, 2, 32, 5, 8], k = 60))
        
