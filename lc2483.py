class Solution:
    def bestClosingTime(self, customers: str) -> int:
        psum = [0] * (len(customers) + 1)
        ssum = [0] * (len(customers) + 1)
        for x in range(0, len(customers)):
            psum[x + 1] = psum[x] + (customers[x] == 'N')
            
            ssum[len(customers) - x - 1] =ssum[len(customers) - x] + (customers[len(customers) - x - 1] == 'Y')

        
        print(psum)
        print(ssum)
        res = 0
        pen = float('inf')
        for x in range(0, len(customers) + 1):
            new_pen = ssum[x] + psum[x]
            if new_pen < pen:
                res = x
                pen = new_pen

        return res



x = Solution()
print(x.bestClosingTime( customers = "YYNY"))

        
