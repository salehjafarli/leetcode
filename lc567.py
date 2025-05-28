class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mpp = {}       
        for ch in s1:
            if mpp.get(ch) is None:
                mpp[ch] = 1
            else:
                mpp[ch] += 1

        l = 0
        #r = 0
        cnt = 0
        tmpp = {}
        for r in range (0,len(s2)):

            #doesnt exist on s1, therefore put s1 to next char
            if mpp.get(s2[r]) is None:
                cnt = 0
                l = r + 1
                tmpp = {}
            else:
                

                if tmpp.get(s2[r]) is None:
                    tmpp[s2[r]] = 1
                else:
                    tmpp[s2[r]] += 1
                cnt += 1

                #abb -s1
                #baabb-s2
                #two a's in s2 but should be 1, reduce window size from left until a's become 1,
                #then keep expand from right as usual
                while tmpp[s2[r]] > mpp[s2[r]]:
                    tmpp[s2[l]] -= 1
                    cnt -= 1
                    l += 1

                if cnt == len(s1):
                    return True

        return False



    #sucks because copying dic all the time
    #also not using reduce-expand, but rather set r back to l and recalculate, what a joke
    def checkInclusionstupid(self, s1: str, s2: str) -> bool:
        mpp = {}       
        for ch in s1:
            if mpp.get(ch) is None:
                mpp[ch] = 1
            else:
                mpp[ch] += 1

        l = 1
        r = 0
        cnt = 0
        tmpp = mpp.copy()
        while r < len(s2):
            if tmpp.get(s2[r]) is None:
                cnt = 0
                l = r + 1
                r += 1
                tmpp = mpp.copy()
                continue
            else:
                tmpp[s2[r]] -= 1
                cnt += 1
                if tmpp[s2[r]] == -1:
                    cnt = 0 
                    r = l
                    l += 1
                    tmpp = mpp.copy()
                    continue

            if cnt == len(s1):
                return True

            r += 1

        return False



    




x = Solution()

#print(x.checkInclusion(s1 = "ab", s2 = "eidbaooo"))


#print(x.checkInclusion(s1 = "abb", s2 = "baabb"))


print(x.checkInclusion(s1 = "mart", s2 = "karma"))
        
