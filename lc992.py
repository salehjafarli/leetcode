class Solution:
    def subarraysWithKDistinct(self, nums, k: int) -> int:
        return self.atMostK(nums, k)  - self.atMostK(nums, k - 1)
        pass

    def atMostK(self, nums, k):
        l = res = 0
        mpp = {}
        for r in range(0, len(nums)):
            if mpp.get(nums[r], 0) == 0:
                mpp[nums[r]] = 1
                k -= 1
            else:
                mpp[nums[r]] += 1

            while k < 0:
                mpp[nums[l]] -= 1
                res += r - l
                #print(r - l)
                if mpp[nums[l]] == 0:
                    k += 1
                l += 1
        if r >= l:
            res += (r - l + 1) * (r - l + 2) // 2
        return res



        


        

x = Solution()
print(x.subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2))



print(x.subarraysWithKDistinct(nums = [1,2,1,3,4], k = 3))


#print(x.subarraysWithKDistinct(nums = [2,1,1,1,2], k = 1))

#print(x.subarraysWithKDistinct(nums = [1,1,1,1,2,1,1], k = 2))
        
