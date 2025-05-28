class Solution:
    def minMoves(self, nums, limit: int) -> int:
        targets = [0] * (limit * 2 + 2)
        for x in range(0, len(nums) // 2):
            a = nums[x]
            b = nums[-x - 1]
            
            targets[2] += 2
            targets[min(a, b) + 1] += -2

            targets[min(a, b) + 1] += 1
            targets[a + b] -= 1
            
            targets[a + b + 1] += 1
            targets[max(a, b) + limit + 1] -= 1

            targets[max(a, b) + limit + 1] += 2
        
        
        res = 9999999
        for x in range(2, len(targets) - 1):
            targets[x] += targets[x - 1]
            res = min(targets[x], res)

        print(targets)

        return res




x = Solution()

#print(x.minMoves(nums = [1,2,4,3], limit = 4))

print(x.minMoves(nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], limit = 1))




        
