class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def calculateChar(ch, s, k):
            rem_k = k
            max_ln = 0
            ln = 0
            l = 0
            for r in range(0, len(s)):
                if rem_k > 0 and s[r] != ch:
                    rem_k -= 1
                elif rem_k == 0 and s[r] != ch:
                    #print(ln)
                    #print(s[l:r])
                    max_ln = max(max_ln, ln)
                    brk = True
                    while brk:
                        if s[l] != ch:
                            brk = False
                        l += 1
                        ln -= 1
                ln += 1
            return max(max_ln, ln)
        
        res = 0
        known_chrs = {}

        for ch in s:
            if known_chrs.get(ch) is None:
                known_chrs[ch] = 1

        for ch in known_chrs.keys():
            temp = calculateChar(ch, s, k)
            res = max(res, temp)
        return res





x = Solution()
#print(x.characterReplacement(s = "AABABBA", k = 1))

print(x.characterReplacement(s = "AAAB", k = 0))

print(x.characterReplacement(s = "ABCDEAAAAFAAAA", k = 3))
        
