from collections import deque 
class Solution:
    def countSubarrays(self, nums, minK: int, maxK: int) -> int:
        if minK > maxK:
            return 0
        elif minK == maxK:
            res = 0
            lim = 0
            for i in range(0, len(nums)):
                if nums[i] != minK:
                    res += lim * (lim + 1) // 2
                    lim = 0
                    continue
                lim += 1
            return res + lim * (lim + 1) // 2
        

        res = 0
        sum = 0
        pending_sum = 0
        l = 0
        max_hit = min_hit = False
        prev_ind = 0
        for i in range(0, len(nums)):
            if nums[i] == minK:
                min_hit = True
                if min_hit and max_hit:
                    ln = i - l
                    l = prev_ind + 1
                    res += ln * (ln + 1) // 2
                    print(res, ln)
                    ln = i - l
                    res -= ln * (ln + 1) // 2
                    print(res, ln)
                    max_hit = False
                prev_ind = i
            elif nums[i] == maxK:
                max_hit = True
                if min_hit and max_hit:
                    ln = i - l
                    l = prev_ind + 1
                    res += ln * (ln + 1) // 2
                    print(res, ln)
                    ln = i - l
                    res -= ln * (ln + 1) // 2
                    print(res, ln)
                    min_hit = False
                prev_ind = i

            elif nums[i] < minK or nums[i] > maxK:
                res += len(nums) - i
        
        ln = i - l + 1
        res += ln * (ln + 1) // 2
        print(res, ln)
            

        return len(nums) * (len(nums) + 1) // 2 - res

    def brute(self, nums, minK: int, maxK: int):
        cnt = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums) + 1):
                slc = nums[i:j]
                if min(slc) != minK or max(slc) != maxK:
                    print(slc)
                    cnt += 1



        print(cnt)



    def countSubarrays2(self, nums, minK: int, maxK: int) -> int:
        if minK > maxK:
            return 0
        elif minK == maxK:
            res = 0
            lim = 0
            for i in range(0, len(nums)):
                if nums[i] != minK:
                    res += lim * (lim + 1) // 2
                    lim = 0
                    continue
                lim += 1
            return res + lim * (lim + 1) // 2
        

        res = 0
        sum = 0
        pending_sum = 0
        l = - 1
        hit = False
        for i in range(0, len(nums)):
            if nums[i] == minK:
                if l > -1:
                    if nums[l] == maxK:
                        hit = True
                        sum += pending_sum
                        pending_sum = 0
                    
                    pending_sum += i - l
                l = i 
            elif nums[i] == maxK:
                if l > -1:
                    if nums[l] == minK:
                        hit = True
                        sum += pending_sum
                        pending_sum = 0
                    
                    pending_sum += i - l
                l = i

            if nums[i] > maxK or nums[i] < minK:
                sum = 0
                pending_sum = 0
                hit = False

            if hit:
                res += 1 + sum
            print(sum)
            
        return res







x = Solution()        
#print(x.countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))
#print(x.countSubarrays(nums = [1,2,1,3,2,5,5,6,7], minK = 1, maxK = 5))
#print(x.countSubarrays(nums = [1,2,1,1], minK = 1, maxK = 1))

#print(x.countSubarrays(nums =[76, 30, 100, 1, 100, 71, 92, 94, 100, 1, 62, 53, 52, 47, 60, 1, 1, 1, 1, 1], minK = 1, maxK = 100))



#print(x.countSubarrays(nums =[1, 40, 100, 100, 90, 100, 1, 100, 16, 100, 1, 8, 86, 44, 57], minK = 1, maxK = 100))

print(x.countSubarrays(nums =[101, 100, 53, 4, 1, 1, 5, 100, 1, 100, 1, 47, 1, 100, 1, 100, 26, 1], minK = 1, maxK = 100))

#print(x.brute(nums =[1, 40, 100, 100, 90, 100, 1, 100, 16, 100, 1, 8, 86, 44, 57], minK = 1, maxK = 100))




