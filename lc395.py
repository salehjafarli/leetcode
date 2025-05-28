class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        mpp = {}

        for r in range(0, len(s)):
            ch = s[r]
            mpp[ch] = mpp.get(ch, 0) + 1
        

        def calculateLongest(l ,r, mapp, s):
            res = 0
            freqs = {}
            print(s[l:r])
            print(mapp)
            for i in range(l, r):
                if mapp.get(s[i], 0) < k:
                    l = i + 1
                    freqs = {}
                else:
                    freqs[s[i]] = freqs.get(s[i], 0) + 1
                    print(l) 
                    for v in freqs.values():
                        if v < k:
                            break
                    else:
                        res = max(res, i - l + 1)
            return res


        mpp2 = {}
        l = 0
        for r in range(0, len(s)):
            ch = s[r]
            if mpp[ch] < k:
                res = max(res, calculateLongest(l, r, mpp2, s))
                mpp2 = {}
                l = r + 1
            else: 
                mpp2[ch] = mpp2.get(ch, 0) + 1
        
        res = max(res, calculateLongest(l, r + 1, mpp2, s))
        return res
                


x = Solution()
#print(x.longestSubstring( s = "caaabbc", k = 3))

#print(x.longestSubstring( s = "bbaaacbd", k = 3))
            
#print(x.longestSubstring( s = "baaabcb", k = 3))


print(x.longestSubstring( s = "abcdcdcdbafba", k = 3))



#print(x.longestSubstring( s = "aacbbbdc", k = 2))




