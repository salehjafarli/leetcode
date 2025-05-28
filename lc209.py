class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        l = sum = 0
        res = len(nums) + 1

        for r in range(0, len(nums)):
            sum += nums[r]

            while sum >= target:
                res = min(res, r - l  + 1)
                sum -= nums[l]
                l += 1
            

        while sum >= target:
            res = min(res, len(nums) - l)
            sum -= nums[l]
            l += 1
        
        return res if res <= len(nums) else 0



x = Solution()
print(x.minSubArrayLen(target = 11, nums =[1, 2, 3, 4, 5])) #3
print(x.minSubArrayLen(target = 15, nums =[5,1,3,5,10,7,4,9,2,8]))  #2


        
