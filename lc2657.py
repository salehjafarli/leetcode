class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        res = [0] * len(A)
        mppA = [False] * (len(A) + 1)
        mppB = [False] * (len(A) + 1)
        for i in range(0, len(A)):
            mppA[A[i]] = True
            mppB[B[i]] = True
            res[i] = res[i - 1] 
            if mppA[B[i]]:
                res[i] += 1
            if B[i] != A[i] and mppB[A[i]]:
                res[i] += 1

        return res



x = Solution()
A = [1,3,2,4] 
B = [3,1,2,4]
print(x.findThePrefixCommonArray(A, B))
        