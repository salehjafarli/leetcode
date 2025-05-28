class Solution:
    def longestAlternatingSubarray(self, nums, threshold: int) -> int:
        if len(nums) == 1:
            return ((nums[0] % 2) ^ 1) & int(nums[0] <= threshold)

        rem = cnt = res = 0
        for r in range(0, len(nums)):
            if nums[r] > threshold:
                res = max(res, cnt)
                cnt = rem = 0
                continue

            if nums[r] % 2 == rem:
                cnt += 1
                rem ^= 1
            else:
                #rem is 1, double evens, start from 2nd even thats why cnt is 1
                #rem is 0, double odds, ignore both thats why cnt is 0
                res = max(res, cnt)
                cnt = rem

        

        res = max(res, cnt)
        return res



x = Solution()
#print(x.longestAlternatingSubarray(nums = [3,2,5,4], threshold = 5))
        
print(x.longestAlternatingSubarray(nums = [4, 10, 3], threshold = 10))
