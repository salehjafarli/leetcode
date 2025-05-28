class Solution:
    def numTilings(self, n: int) -> int:
        mp = {1: 1, 2: 2, 3: 5}
        return self.numTilingsRecursive(n, mp) % (10 ** 9 + 7)
        

    def numTilingsRecursive(self, n, mpp):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 5
        
        res = self.numTilingsRecursive(n - 1, mpp) * 2 + mpp[n - 3]
        mpp[n] = res

        return res





x = Solution()
print(x.numTilings(4))
        
