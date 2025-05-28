class Solution:

    def minDominoRotations(self, tops, bottoms) -> int:
        arr = [0] * 7 
        arr2 = [0] * 7 
        same = [0] * 7

        cnt = 0
        i = -1
        for x in range(0, len(tops)):
            top = tops[x]
            bottom = bottoms[x]
            if top != bottom:
                arr[top] += 1
                arr2[bottom] += 1
            else:
                same[top] += 1
            

            temp = arr[top] + arr2[top] + same[top]
            temp2 = arr[bottom] + arr2[bottom] + same[bottom]
            #print(top, temp, bottom, temp2) 

            if temp == len(tops):
                return min(arr[top], arr2[top])
            elif temp2 == len(bottoms):
                return min(arr[bottom], arr2[bottom])
            

        return -1 
        

    def minDominoRotations2(self, tops, bottoms) -> int:
        arr = [0] * 7 
        for x in range(0, len(tops)):
            arr[tops[x]] += 1
            if tops[x] != bottoms[x]:
                arr[bottoms[x]] += 1
        
        mx = i = 0
        for x in range(0, len(arr)):
            if arr[x] > mx:
                mx = arr[x]
                i = x

        tm = bm = 0
        for x in range(0, len(tops)):
            if tops[x] == bottoms[x] == i:
                continue

            if tops[x] == i:
                bm += 1
            elif bottoms[x] == i:
                tm += 1
            else:
                return -1


        return min(tm, bm)

        

        
     


x = Solution()
print(x.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))


#print(x.minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]))
        
#print(x.minDominoRotations(tops = [1, 1, 1], bottoms = [1, 1, 1]))
