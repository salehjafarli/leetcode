class Solution:
    def numberOfSubarrays(self, nums, k: int) -> int:
        sums = [0] * (len(nums) + 1)
        mpp = {0 : 1}
        res = 0
        for r in range(0, len(nums)):
            num = nums[r] % 2
            sums[r + 1] = sums[r] + num
            
            res += mpp.get(sums[r + 1] - k, 0)

            mpp[sums[r + 1]] = mpp.get(sums[r + 1], 0) + 1

        return res





    def numberOfSubarraysSliding(self, nums, k: int) -> int:
        l = res = lres = K = 0

        for r in range(0, len(nums)):
            if nums[r] % 2 == 1:
                K += 1
           
            if K > k:
                while K > k:
                    if nums[l] % 2 == 1:
                        K -= 1
                    l += 1
                    res += lres
                lres = 0


            if K == k:
                lres += 1
        
        while K == k:
            if nums[l] % 2 == 1:
                K -= 1
            l += 1
            res += lres



        return res

            
            
 





x = Solution()
print(x.numberOfSubarrays(nums = [1,1,2,1,1], k = 3))


print(x.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))
       
