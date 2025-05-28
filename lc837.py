class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        arr = [0] * maxPts
        for x in range(1, maxPts + 1):
            arr[x - 1] = x
            
        sum = 0
        count = 0
        l = 0
        for r in range(0, len(arr)):
            sum += arr[r]
            count += r - l + 1

            while sum > k:
                sum -= arr[l]
                l += 1


                if sum < n


        print(arr)





x = Solution()
print(x.new21Game(n = 21, k = 17, maxPts = 10))
        
