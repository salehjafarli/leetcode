class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 1:
            return ""
        elif len(s) == 2:
            return s if abs(ord(s[0]) - ord(s[1])) == 32 else ""

        mpp = {}
        for x in range(0, len(s)):
            c = ord(s[x])
            mpp[c] = 1

        res = "" 
        l = r = 0
        while r < len(s):
            c = ord(s[r])
            if (c < 91 and mpp.get(c + 32, 0) == 0) or (c > 91 and mpp.get(c - 32, 0) == 0):
                st = self.longestNiceSubstring(s[l:r])
                #print(c, l,r, s, st)
                l = r + 1
                if len(st) > len(res):
                    res = st
            r += 1
        
        if r - l == len(s):
            return s

        if r  - l < len(s):
            st = self.longestNiceSubstring(s[l:r])
            if len(st) > len(res):
                return st

        return res


x = Solution()
print(x.longestNiceSubstring(s = "XqLJWaEEcAjslIXxKZgufikxFwVVYUlvYrIeGRyS"))
        
