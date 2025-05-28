class Solution:
    def maxTotalFruits(self, fruits, startPos: int, k: int) -> int:
        leftSums = [0] * (k + 1)
        rightSums = [0] * (k + 1)
        posAmt = 0
        for pos, amt in fruits:
            if pos < startPos and startPos - pos < k + 1:
                leftSums[startPos - pos] = amt
            elif pos == startPos:
                posAmt = amt
                if k == 0:
                    return posAmt
            elif pos > startPos and pos - startPos < k + 1:
                rightSums[pos - startPos] = amt
            
        for x in range(1, len(leftSums)): 
            leftSums[x] += leftSums[x - 1]
            rightSums[x] += rightSums[x - 1]
        
        #print(leftSums, rightSums)
        res = onlyLeft = onlyRight = leftRight = rightLeft = 0
        for x in range(1, len(leftSums)):
            onlyLeft = leftSums[x]
            onlyRight = rightSums[x]
            
            if x * 2 < k:
                leftRight = onlyLeft + rightSums[k - x * 2]
                rightLeft = onlyRight + leftSums[k - x * 2]

            res = max(res, onlyLeft, onlyRight, leftRight, rightLeft)

        return res + posAmt


x = Solution()
#print(x.maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4))

print(x.maxTotalFruits(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4))
            
        
