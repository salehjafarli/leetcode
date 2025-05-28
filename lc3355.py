class Solution:
    def isZeroArray(self, nums, queries) -> bool:
        sums = [0] * len(nums)
        for query in queries:
            l, r = query
            sums[l] -=  1
            if r + 1 < len(nums):
                sums[r + 1] += 1

        
        sum = 0
        #print(sums)
        for q in range(0, len(sums)):
            sum += sums[q]
            new_num = nums[q] + sum
            #print(sum, new_num)

            if new_num > 0:
                return False


        return True



x = Solution()
print(x.isZeroArray(nums = [4,3,2,1], queries = [[1,3],[0,2]]))
