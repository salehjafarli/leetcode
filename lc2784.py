class Solution:
    def isGood(self, nums: List[int]) -> bool:
        mx = max(nums)
        l = len(nums)

        if (mx + 1) != l:
            return False

        st = set()
        mxcnt = 0
        for x in nums:
            if x == mx:
                mxcnt += 1
                if mxcnt > 2:
                    return False
                continue
            if x in st:
                return False
            st.add(x)
            
        return True




        
#nums = [3, 4, 4, 1, 2, 1]
nums = [2,2,2]
x = Solution()
print(x.isGood(nums))