class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        diffs = [0] * len(word)
        for r in range(1, len(word)):
            diffs[r] = abs(ord(word[r]) - ord(word[r - 1]))

        print(diffs)



x = Solution()
#print(x.countCompleteSubstrings(word = "igigee", k = 2))


print(x.countCompleteSubstrings(word = "aaabbbccc", k = 3))

        
