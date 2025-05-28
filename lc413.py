class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        if len(nums) < 3:
            return 0

        def allPossible(l, r):
            slice_len = r - l + 1 - 2
            return (slice_len * (slice_len + 1)) // 2
            
        
        res = 0
        l = 0
        r = 1
        diff = 9999
        while r < len(nums):
            temp = nums[r] - nums[r - 1]
            if r - l > 1 and temp != diff:
                res += allPossible(l, r - 1) 
                l = r - 1
                
            elif r == len(nums) - 1 and r - l > 1:
                res += allPossible(l, r) 
                break
 
            diff = temp
            r += 1


        return res



    def numberOfArithmeticSlices2(self, nums) -> int:
        if len(nums) < 3:
            return 0
        
        res = 0
        diff = 9999
        for l in range(0, len(nums) - 2):
            for r in range(l + 1, len(nums)):
                temp = nums[r] - nums[r - 1]
                if temp == diff and r - l > 1:
                    res += 1   
                elif r - l > 1 and temp != diff:
                    break
                diff = temp
        return res




x = Solution()


print(x.numberOfArithmeticSlices([1, 2, 3, 4, 9, 13]))
