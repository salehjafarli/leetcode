class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        mpp = {}
        for r in range(0, len(nums)):
            ra = mpp.get(nums[r])
            if ra is not None and ra - r + 1 <= k:
                return True

            mpp[nums[r]] = r
        return False











x = Solution()
print(x.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
        
