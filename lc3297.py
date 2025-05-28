class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        m2 = {}
        for x in range(0, len(word2)):
            m2[word2[x]] = m2.get(word2[x], 0) + 1

        cnt = len(word2)
        m1 = {}
        l = res = 0
        for r in range(0, len(word1)):
            if word1[r] in m2:
                m1[word1[r]] = m1.get(word1[r], 0) + 1

                if m1[word1[r]] <= m2[word1[r]]:
                    cnt -= 1

            
            while cnt == 0:
                res += len(word1) - r
                if word1[l] in m2:
                    m1[word1[l]] -= 1

                    if m1[word1[l]] < m2[word1[l]]:
                        cnt += 1
                l += 1



        return res



x = Solution()

#print(x.validSubstringCount("abcabc", word2 = "abc"))

#print(x.validSubstringCount(word1 = "abcabc", word2 = "aaabc"))



print(x.validSubstringCount(word1 = "dcbdcdccb", word2 = "cdd"))
