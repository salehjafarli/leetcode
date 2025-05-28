class Solution:
    def findAnagrams(self, s: str, p: str) -> bool:
        mpp = {}       
        for ch in p:
            if mpp.get(ch) is None:
                mpp[ch] = 1
            else:
                mpp[ch] += 1
        
        res = []
        l = 0
        #r = 0
        cnt = 0
        tmpp = {}
        for r in range (0,len(s)):
            #doesnt exist on s1, therefore put s1 to next char
            if mpp.get(s[r]) is None:
                cnt = 0
                l = r + 1
                tmpp = {}
            else:
                

                if tmpp.get(s[r]) is None:
                    tmpp[s[r]] = 1
                else:
                    tmpp[s[r]] += 1
                cnt += 1

                #abb -s1
                #baabb-s2
                #two a's in s2 but should be 1, reduce window size from left until a's become 1,
                #then keep expand from right as usual
                while tmpp[s[r]] > mpp[s[r]]:
                    tmpp[s[l]] -= 1
                    cnt -= 1
                    l += 1

                if cnt == len(p):
                    res.append(l)

            


        return res




x = Solution()
print(x.findAnagrams(s = "cbaebabacd", p = "abc"))
