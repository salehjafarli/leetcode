class Solution:
    def productExceptSelf(self, nums):
        res = [0] * len(nums)
        prefixProduct = [1] * len(nums)
        postfixProduct = [1] * len(nums)

        
        for x in range(1, len(nums)):
            prefixProduct[x] = prefixProduct[x - 1] * nums[x - 1]
            postfixProduct[len(nums) - x - 1] =  postfixProduct[len(nums) - x] * nums[len(nums) - x]

        
        for x in range(0, len(prefixProduct)):
            res[x] = prefixProduct[x] * postfixProduct[x]



        return res

    def productExceptSelf1(self, nums):
        res = [0] * len(nums)
        
        product = 1
        zc  = 0
        for x in range(0, len(nums)):
            if nums[x] == 0:
                zc += 1
                if zc == 2:
                    return res
                continue

            product *= nums[x]


        for x in range(0, len(res)):
            if nums[x] == 0:
                res[x] = product
            elif zc == 1:
                res[x] = 0
            else:
                res[x] = product // nums[x]



        return res



x = Solution()
print(x.productExceptSelf(nums = [1,2,3,4]))


#print(x.productExceptSelf(nums = [-1,1,0,-3,3]))
        
