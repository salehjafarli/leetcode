class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mpp = {}
        l = res = cnt = 0
        for r in range(0, len(s)):
            mpp[s[r]] = mpp.get(s[r], 0) + 1

            while mpp[s[r]] > 2:
                mpp[s[l]] -= 1
                l += 1
                cnt -= 1

            cnt += 1
            res = max(res, cnt) 
        return res


x = Solution()
print(x.maximumLengthSubstring(s = "bcbbbcba"))
        
