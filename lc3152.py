class Solution:
    def isArraySpecial(self, nums, queries):
        sums = [0] * (len(nums))
        for x in range(1, len(nums)):
            s = nums[x] % 2 == nums[x - 1] % 2
            sums[x] = sums[x - 1] + s
        
        print(nums)
        print(sums)
        res = [] 
        for f,t in queries:
            res.append(sums[t] - sums[f] == 0)


        return res

x = Solution()
print(x.isArraySpecial(nums = [3,4,1,2,6,3,4,3,4], queries = [[0,4]]))

        
