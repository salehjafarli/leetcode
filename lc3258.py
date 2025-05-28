class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l = res = 0
        mpp = {'0' : 0, '1' : 0}
        cnt = 0
        for r in range(0, len(s)):
            mpp[s[r]] += 1 

            while mpp['0'] > k and mpp['1'] > k:
                cnt += len(s) - r 
                mpp[s[l]] -= 1
                l += 1

            res += 1
        
        return len(s) * (len(s) + 1) // 2 - cnt
        

x = Solution()
print(x.countKConstraintSubstrings(s = "10101", k = 1))
        
