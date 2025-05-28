

class RollingHash():
    def __init__(self, string, p = 31, m = 10 ** 9 + 9):
        self.curr_pow = 1
        self.p = p
        self.m = m
        temp_hash = 0
        for ch in string:
            temp_hash = (temp_hash + ord(ch) * self.curr_pow ) % m
            self.curr_pow = (self.curr_pow * p ) % m 
            

        self.hash = temp_hash


    
    def modinv(p, m):
        return math.pow(p, m-2, m)  # Fermat's Little Theorem


        
    def strip(self, ch):
        self.hash = (self.hash - ord(ch) + self.m) % self.m
        p_inv = pow(self.p, self.m - 2, self.m)

        self.hash = (self.hash * p_inv) % self.m
        self.curr_pow = (self.curr_pow * p_inv) % self.m 

    def add(self, ch):
        self.hash = (self.hash + ord(ch) * self.curr_pow ) % self.m
        self.curr_pow = (self.curr_pow * self.p ) % self.m 







class Solution:
    def findRepeatedDnaSequences(self, s: str):
        if len(s) < 10:
            return []


        res = [] 
        dic = {}        
        hash = RollingHash(s[:10])

        dic[hash] = 1
        l = 0
        
        print(s[:10], hash.hash)


        for r in range(11, len(s)):
            hash.strip(s[l])
            hash.add(s[r])
            l += 1

            print(s[l:r], hash.hash)

            if dic.get(hash.hash) is not None:
                res.append(s[l:r])

        return res






x = Solution()

print(x.findRepeatedDnaSequences(s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
        
