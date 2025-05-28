class Solution:
    def splitPainting(self, segments):
        mpp = {}
        for si in range(0, len(segments)):
            seg = segments[si]

            mpp[seg[0]] = mpp.get(seg[0], 0) + seg[2]
            mpp[seg[1]] = mpp.get(seg[1], 0) - seg[2]

        l = sum = 0
        res = []
        for r in sorted(mpp):
            if l != 0 and sum != 0:
                res.append([l, r, sum])

            sum += mpp[r] 
            l = r
        return res


    def splitPainting1(self, segments):
        sums = [0] * 100001
            
        #sums = [0] * 22
        seg_ends = {}
        start = 10 ** 5

        for si in range(0, len(segments)):
            seg = segments[si]

            seg_ends[seg[0]] = 1
            seg_ends[seg[1]] = 1
            
            start = min(start, seg[0])

            sums[seg[0]] += seg[2]
            if seg[1] < len(sums): sums[seg[1]] += -seg[2]
        
        print(seg_ends)
        print(sums)
        print(start)

        res = []
        l = start
        sum = sums[start]
        for r in range(start + 1, len(sums)):
            if seg_ends.get(r) is not None:
                if sum > 0:
                    res.append([l, r, sum])
                l = r

            sum += sums[r]

        return res







x = Solution()
print(x.splitPainting(segments = [[1,4,5],[4,7,7],[1,7,9]]))


print(x.splitPainting(segments = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]))


#print(x.splitPainting(segments = [[1,7,9],[6,8,15],[8,10,7]]))



#print(x.splitPainting(segments = [[4,5,9],[8,12,5],[4,7,19],[14,15,1],[3,10,8],[17,20,18],[7,19,14],[8,16,6],[14,17,7],[11,13,3]]))


#print(x.splitPainting(segments = [[4,16,12],[9,10,15],[18,19,13],[3,13,20],[12,16,3],[2,10,10],[3,11,4],[13,16,6]]))

