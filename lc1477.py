class Solution:
    def minSumOfLengths(self, arr, target):
        sum = l = 0
        sarrs = []

        for r in range(0, len(arr)):
            sum += arr[r]

            while sum > target:
                sum -= arr[l]
                l += 1

            if sum == target:
                sarrs.append((l, r))

        if len(sarrs) < 2:
            return -1
        
        print(sarrs)
        res = 9999
        found = False

        #TLE: Fix it
        for i in range(0, len(sarrs)):
            for j in range(0, len(sarrs)):
                if sarrs[i][1] < sarrs[j][0] or sarrs[i][0] > sarrs[j][1]:
                    found = True
                    lni = sarrs[i][1] - sarrs[i][0] + 1
                    lnj = sarrs[j][1] - sarrs[j][0] + 1
                    res = min(res, lni + lnj)

        return res if found else -1


x = Solution()
print(x.minSumOfLengths([3,2,1,4,3], 3))
