class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = cnt = 0
        res = 999999
        
        for r in range(0, k - 1):
            if blocks[r] == 'W':
                cnt += 1

        for r in range(k - 1, len(blocks)):
            if blocks[r] == 'W':
                cnt += 1

            res = min(res, cnt)
            if blocks[l] == 'W':
                cnt -= 1
            l += 1
        return res







x = Solution()
print(x.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))

        
