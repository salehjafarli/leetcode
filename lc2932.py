class Solution:


    def maximumStrongPairXor(self, nums) -> int:
        nums.sort()
        i = res = 0


        for j in range(1, len(nums)):
            print(i, j)
            if nums[j] - nums[i] <= min(nums[j], nums[i]):
                res = max(res, nums[j] ^ nums[i])
            else:
                i += 1
            
            temp = i
            while j > temp:
                print(temp, j)
                if nums[j] - nums[temp] <= min(nums[j], nums[temp]):
                    res = max(res, nums[j] ^ nums[temp])
                temp += 1


        return res


    def maximumStrongPairXor2(self, nums) -> int:
        nums.sort()
        l = res = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] - nums[i] <= min(nums[j], nums[i]):
                    res = max(res, nums[j] ^ nums[i])

        return res


x = Solution()
print(x.maximumStrongPairXor(nums = [1,4,5,5,7]))
        
