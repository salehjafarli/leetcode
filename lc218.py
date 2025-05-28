class Solution:
    def getSkyline(self, buildings):
        sums = {}
        for building in buildings:
            l, r, h = building
            
            #sums[l] = sums.get(l, 0) + h
            #sums[r] = sums.get(r, 0) - h

            sums[l] = h
            sums[r] = 0

        
        print(sums)
        l = 0 
        sum = 0
        res = []
        for r in sorted(sums):
            if l != 0:
                res.append([l, sum])

            sum += sums[r]
            l = r

        return res

x = Solution()
print(x.getSkyline(buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))


        
