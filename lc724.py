class Solution:
    def pivotIndex(self, nums) -> int:
        mpp = {}
        prefixsums = [0] * (len(nums))
        postfixsums = [0] * (len(nums))

        for x in range(1, len(nums)):
            y = len(nums) - x - 1

            prefixsums[x] = prefixsums[x - 1] + nums[x - 1]
            postfixsums[y] = postfixsums[y + 1] + nums[y + 1]

        
        for x in range(0, len(prefixsums)):
            if prefixsums[x] == postfixsums[x]:
                return x

        return -1




x = Solution()
print(x.pivotIndex(nums = [1,7,3,6,5,6]))
        
