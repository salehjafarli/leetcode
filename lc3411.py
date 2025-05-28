
import math
class Solution:

    def maxLength(self, nums) -> int:
        l = res = 0
        product = 1

        for r in range(0, len(nums)):

            lcm = math.lcm(product, nums[r])
            gcd = 1 if r - l + 1 != 2 else math.gcd(*nums[l:r + 1])

            while product != lcm * gcd:
                product /= nums[l]
                l += 1
                lcm = math.lcm(product, nums[r])

            product *= nums[r]
            res = max(r - l + 1, res)

            

        return res 



    def maxLength2(self, nums) -> int:
        l = res = 0
        product = 1

        for r in range(0, len(nums)):
            product *= nums[r]

            temp = math.gcd(*nums[l:r + 1]) * math.lcm(*nums[l:r+1])

            #print(nums[l:r+1], product, math.gcd(*nums[l:r + 1]), math.lcm(*nums[l:r+1]) )
            if product == temp:
                res = max(r - l + 1, res)

            while product> temp:
                product /= nums[l]
                l += 1
                temp = math.gcd(*nums[l:r + 1]) * math.lcm(*nums[l:r+1])
                #print(nums[l:r+1], product, math.gcd(*nums[l:r + 1]), math.lcm(*nums[l:r+1]), 'w')


        return res 



x = Solution()
#print(x.maxLength(nums = [1,3,1,2,9,4,1]))



#print(x.maxLength(nums = [6,7,2,1]))
        
print(x.maxLength(nums = [2,6]))
