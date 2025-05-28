class Solution:
    def shiftingLetters(self, s: str, shifts) -> str:
        def shift(char, x):
            char = ord(char)
            rem = x % 26
            if rem > 122 - char:
                char = 96 + rem - (122 - char)
            else:
                char += rem

            return chr(char)

        sums = [0] * len(s)

        for x in range(0, len(shifts)):
            sh = shifts[x]
            sign = (sh[2] << 1) - 1
            sums[sh[0]] += sign
            if sh[1] + 1 < len(s):
                sums[sh[1] + 1] += sign * -1


        sum = 0 
        res = ""
        for x in range(0, len(sums)):
            sum += sums[x]
            res += shift(s[x], sum)

        return res





            






x = Solution()
print(x.shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]))
        
