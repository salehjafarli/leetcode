class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mt = {}
        for x in t:
            mt[x] = mt.get(x, 0) + 1

        cnt = len(t)
        ms = {}
        li = l = 0
        res = 99999
        for r in range(0, len(s)):
            if s[r] in mt:
                ms[s[r]] = ms.get(s[r], 0) + 1
                if ms[s[r]] <= mt[s[r]]:
                    cnt -= 1

            while cnt == 0:
                if s[l] in mt:
                    if res > r - l + 1:
                        res = r - l + 1
                        li = l

                    ms[s[l]] -= 1

                    if ms[s[l]] < mt[s[l]]:
                        cnt += 1
                l += 1
                

        return "" if res == 99999 else s[li:li+res]



x = Solution()
#print(x.minWindow(s = "ADOBECODEBANC", t = "ABC"))


#print(x.minWindow(s = "acbbaca", t = "aba"))


print(x.minWindow(s = "cabwefgewcwaefgcf", t = "cae"))
        
