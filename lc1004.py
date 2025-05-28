class Solution:
    def longestOnes(self, nums, k: int) -> int:
        # PREFIX SUM
        mpp = {0 : 0}
        res = 0
        sums = [0] * (len(nums) + 1)
        for x in range(0, len(nums)):
            sums[x + 1] += sums[x] + (nums[x] ^ 1)
            
            if sums[x + 1] < k:
                res += 1
            else:
                temp = mpp.get(sums[x + 1] - k)
                if temp is not None:
                    res = max(res, x - temp + 1)



            mpp[sums[x + 1]] = min(mpp.get(sums[x + 1], 99999), x + 1)
        

        return res





    def longestOnes_SlidingWindow(self, nums, k: int) -> int:
        if len(nums) == 1:
            return nums[0] | k
        
        K = k
        l = res = cnt = 0
        for r in range(0, len(nums)):
            if nums[r] == 0:
                while K == 0:
                    if nums[l] == 0:
                        K += 1
                    l += 1
                    cnt -= 1
                if K > 0:
                    K -= 1

            cnt += 1 
            res = max(res, cnt) 
            
    
        return res



x = Solution()
print(x.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))


print(x.longestOnes(nums =[0,0,0,1], k = 4))



#print(x.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))
