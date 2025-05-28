class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        mpp = {}

        for dm in dominoes:
            new_p = (dm[0], dm[1]) if dm[1] > dm[0] else (dm[1], dm[0])

            mpp[new_p] = mpp.get(new_p, 0) + 1
        
        res = 0
        for v in mpp.values():
            if v <= 1:
                continue

            res += (v * (v - 1)) // 2

        return res

x = Solution()
print(x.numEquivDominoPairs(dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]))
