
class Solution:
    def twoSum(self, nums, target: int):
        cnts = {}
        for i in range(0, len(nums)):
                cnts[nums[i]] = i


        res = []
        for i in range(0, len(nums)):
            rem = target - nums[i]
            j = cnts.get(rem)
            if j is None:
                continue
            
            if j != i:
                return [i, j]




x = Solution()
#print(x.twoSum(nums = [2,7,11,15], target = 9))

#print(x.twoSum(nums = [3,2,4], target = 6))

        
print(x.twoSum(nums = [3,3], target = 6))
