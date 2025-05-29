
class Solution:
    def maximumLength(self, s: str) -> int:
        l = 1
        r = len(s)
        res = -1
        while l < r:
            m = (r + l) // 2
            print(l, m, r)
            if self.checkWindow(s, m):
                l = m + 1
                res = m 
            else:
                r = m

        
        return res


    def checkWindow(self, s, ln):
        mpp = {}
        l = 0
        for r in range(ln, len(s) + 1):
            sl = s[l:r]
            mpp[sl] = mpp.get(sl, 0) + 1

            if mpp[sl] == 3 and len(set(sl)) == 1:
               return True 
            
            l += 1
            
        return False


x = Solution()


print(x.checkWindow("abcdabcddddabcddddccccbbbbaaaa", 4))

