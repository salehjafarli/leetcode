class Solution:
    def findClosestElements(self, arr, k: int, x: int):
        if k == len(arr):
            return arr

        l = 0
        r = k
        while r < len(arr):
            diffr = abs(arr[r] - x)
            diffl = abs(arr[l] - x)

            if diffl < diffr or diffl == diffr and arr[l] < arr[r]:
                break 

            l += 1
            r += 1

        
        return arr[l:r]



x = Solution()
#print(x.findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3))


#print(x.findClosestElements(arr = [1,1,2,3,4,5], k = 4, x = -1))


print(x.findClosestElements(arr = [1,1,1,10,10, 10], k = 1, x = 9))



        


