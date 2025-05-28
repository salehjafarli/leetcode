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

        res = "" 
        sum = 0
        for x in range(len(shifts) - 1, -1, -1):
            sum += shifts[x]
            res += shift(s[x], sum)

        return res[::-1]




x = Solution()
#print(x.shiftingLetters( s = "abc", shifts = [3,5,9]))


#print(x.shiftingLetters( s = "bad", shifts = [10, 20, 30]))



print(x.shiftingLetters( s = "ruu", shifts = [26, 9, 17]))
       
