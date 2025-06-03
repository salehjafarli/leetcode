class Solution:
    def findLength(self, nums1, nums2):
        l = 1
        r = min(len(nums1), len(nums2))
        res = 0
        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            if self.checkWindow(m, nums1, nums2):
                l = m + 1
                res = m
            else:
                r = m - 1
        return res

    def checkWindow(self, sz, nums1, nums2):
        l = 0
        mpp = {}
        for r in range(sz, len(nums2) + 1):
            mpp[tuple(nums2[l:r])] = True
            l += 1
        
        l = 0
        for r in range(sz, len(nums1) + 1):
            if mpp.get(tuple(nums1[l:r]), False):
                return True
            l += 1
        return False



x = Solution()

#print(x.checkWindow(3, [5,67,7,78,8, 1,2,3], [1,2,41,45, 1,2,3, 4]))


print(x.findLength([1,2,3,2,1], [3,2,1,4,7]))
