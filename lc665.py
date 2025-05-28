class Solution:
    def checkPossibility(self, nums) -> bool:
        for r in range(1, len(nums)):
            if nums[r - 1] > nums[r]:
                if r - 1 == 0 or nums[r] >= nums[r - 2]:
                    temp = nums[r - 1]
                    nums[r - 1] == nums[r]
                    res = self.checkPossibilityInternal(nums[r:])
                    if res:
                        return True
                    nums[r - 1] = temp

                nums[r] = nums[r - 1]
                res = self.checkPossibilityInternal(nums[r:])
                return res 
                    


        return True 


    def checkPossibilityInternal(self, nums) -> bool:
        for r in range(1, len(nums)):
            if nums[r - 1] > nums[r]:
                return False

        return True 
        


x = Solution()
print(x.checkPossibility([3,4,2,3]))


print(x.checkPossibility([4, 2, 3]))


print(x.checkPossibility([-1,4,2,3]))
