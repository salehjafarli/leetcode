class Solution:
    def merge(self, intervals):
        sums = {}
        for x in range(0, len(intervals)):
            l,r  = intervals[x]
            sums[l] = sums.get(l, 0) + 1
            sums[r] = sums.get(r, 0) - 1
        
        cnt = 0
        l = 0
        res = []
        #print(sums)
        for r in sorted(sums.keys()):
            if cnt == 0:
                l = r

            cnt += sums[r]  
            
            if cnt == 0:
                res.append([l, r])


        return res



x = Solution()
print(x.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))

print(x.merge(intervals = [[1,4],[5,6]]))


print(x.merge(intervals = [[1,4],[0,4]]))
