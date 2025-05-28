class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = l = res = 0
        mpp = {}
        for r in range(0, len(s)):
            ch = s[r]
            if mpp.get(ch, 0) == 0:
                cnt += 1
                mpp[ch] = 1
            else:
                mpp[ch] += 1

            while cnt == 3:
                res += len(s) - r
                mpp[s[l]] -= 1
                if mpp[s[l]] == 0:
                    cnt -= 1
                l += 1

        return res


x = Solution()
print(x.numberOfSubstrings(s = "abcabc"))


        
