class Solution:
    def maxFrequency(self, nums, k: int) -> int:
        nums.sort()

        sums = [0] * (len(nums) + 1)

        for i in range(0, len(nums)):
            sums[i + 1] = sums[i] + nums[i]
        
        print(sums)
        
        l = 0
        res = 1
        r = len(nums) - 1
        while l < r:
            mid = (r - l + 1) // 2 + l 
            
            print(l, mid, r)
            if self.check(mid, k, sums, nums):
                l = mid
                res = mid + 1
            else:
                r = mid - 1
                

        return res


    def check(self, mid, k, sums, nums):
        l = 0
        for r in range(mid, len(nums)):
            sum = sums[r + 1] - sums[l]
            if nums[r] * (r - l + 1) - sum <= k:
                return True
            l += 1

        return False


    def maxFrequencySliding(self, nums, k: int) -> int:
        nums.sort()
        
        diffs = l = 0
        res = 1
        for r in range(1, len(nums)):
            diff = nums[r] - nums[r - 1]
            k -= (r - l) * diff
                        
            while k < 0:
                diff = nums[r] - nums[l]
                k += diff
                l += 1
            
            res = max(res, r - l + 1)

        return res



x = Solution()

print(x.maxFrequency(nums = [1,2,4,4,4,4], k = 5))


#print(x.maxFrequency(nums = [1,4,8,13], k = 5))



        
