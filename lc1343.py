class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        res = l = sum = 0
        K = k
        for r in range(0, len(arr)):
            sum += arr[r]
            if k > 1:
                k -= 1
            else:
                res += 1 if (sum // K) >= threshold else 0

                sum -= arr[l]
                l += 1

        return res


x = Solution()
print(x.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))

