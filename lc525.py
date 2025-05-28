class Solution:
    def findMaxLength(self, nums) -> int:
        res = 0
        mpp = {}
        sums = - 1 if nums[0] == 0 else 1
        mpp[sums] = 0
        for r in range(1, len(nums)):
            if nums[r] == 0:
                sums -= 1
            else:
                sums += 1
            
            if sums == 0:
                res = max(res, r + 1)
                continue
            if mpp.get(sums) is None:
                mpp[sums] = r
            else:
                res = max(res, r - mpp[sums])


        return res


x = Solution()
print(x.findMaxLength(nums = [0,1,1,1,1,1,0,0,0]))


print(x.findMaxLength(nums = [0,0,0,1,1,1,0]))

#print(x.findMaxLength(nums = [0,0,1]))

        
        
