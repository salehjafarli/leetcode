class Solution:
    def shiftDistance(self, s: str, t: str, nextCost, previousCost) -> int:
        def shift(char1, char2, direction, costs):
            diff = char2 - char1
            if diff == 0:
                return 0

            if direction:
                if diff > 0:
                    return costs[char2] - costs[char1]
                else:
                    return costs[25] - costs[char1] + costs[char2] - costs[0]
            else:
                if diff < 0:
                    return costs[char1] - costs[char2]
                else:
                    return costs[char1] - costs[0] + costs[25] - costs[char2]

            

        cost = 0


        nc = [0] * 27
        pc = [0] * 27
        
        for x in range(1, 27):
            nc[x] = nc[x - 1] + nextCost[x - 1]
            pc[26 - x] = pc[27 - x] + previousCost[26 - x]

        print(nc)
        print(pc)

        for x in range(0, len(s)):
            char1 = ord(s[x]) - 97
            char2 = ord(t[x]) - 97
            cost += min(shift(char1, char2, True, nextCost),
                    shift(char1, char2, False, previousCost))

            print(cost)

        return cost



x = Solution()
print(x.shiftDistance(s = "abab", t = "baba", nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))



#print(x.shiftDistance(s = "leet", t = "code", nextCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], previousCost = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))
        
