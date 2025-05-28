class Solution:
    def countCompleteSubarrays(self, nums) -> int:
        mpp = {}
        cnt = 0
        for r in range(0, len(nums)):
            if mpp.get(nums[r]) is None:
                cnt += 1
                mpp[nums[r]] = 1

        return self.atMostK(nums, cnt) - self.atMostK(nums, cnt - 1)

    def atMostK(self, nums, k):
        mpp = [0] * 2001
        l = res = 0
        for r in range(0, len(nums)):
            if mpp[nums[r]] == 0:
                k -= 1

            mpp[nums[r]] += 1

            while k < 0:
                mpp[nums[l]] -= 1
                #print(r - l)
                if mpp[nums[l]] == 0:
                    k += 1
                l += 1

            res += r - l + 1

        return res



x = Solution()
print(x.countCompleteSubarrays(nums = [1,3,1,2,2]))

        
