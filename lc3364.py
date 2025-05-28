class Solution:
    def minimumSumSubarray(self, nums, l: int, r: int) -> int:
        L = sum = 0
        for R in range(0, l):
            sum += nums[R]
        
        res = sum if sum > 0 else 999999

        for R in range(l, len(nums)):
            ln = R - L + 1

            if ln == l:
                sum += nums[R]
            else:
                if ln > r:
                    sum -= nums[L]
                    L += 1
                    ln -= 1

                sum += nums[R]
                while ln > l:
                    removeLeft = sum - nums[L]
                    print(removeLeft, sum)

                    if sum < 0 and removeLeft > 0:
                        sum = removeLeft
                        L += 1
                        ln -= 1
                    elif removeLeft < 0 and sum > 0:
                        break 
                    elif removeLeft < 0 and sum < 0:
                        break

                    if sum > removeLeft:
                        sum = removeLeft
                        L += 1
                        ln -= 1 
                    elif sum <= removeLeft:
                        break

            if res > sum > 0:
               res = sum

        return res if res != 999999 else -1

x = Solution()



#print(x.minimumSumSubarray(nums = [3, -1, 1, 4], l = 2, r = 3))

#print(x.minimumSumSubarray(nums = [-12, 8], l = 1, r = 1))
        
#print(x.minimumSumSubarray(nums = [1,2,3,4], l = 2, r = 4))


#print(x.minimumSumSubarray(nums = [-3, 17], l = 1, r = 2))

#print(x.minimumSumSubarray(nums = [5, 8, -6], l = 1, r = 3))


#print(x.minimumSumSubarray(nums = [-18, 6, 9], l = 1, r = 3))

print(x.minimumSumSubarray(nums = [17, 13], l = 1, r = 2))
