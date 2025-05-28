class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        strnum = str(num)
        l = res = 0
        for r in range(k - 1, len(strnum)):
            subnum = int(strnum[l:r+1])
            if subnum != 0 and num % subnum == 0:
                res += 1
            l += 1
        return res




x =  Solution()
print(x.divisorSubstrings(num = 430043, k = 2))
