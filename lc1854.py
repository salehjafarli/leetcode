class Solution:
    def maximumPopulation(self, logs) -> int:
        sums = [0] * 101
        for x in range(0, len(logs)):
            log = logs[x]
            sums[log[0] - 1950] += 1
            if log[1] < 2050:
                sums[log[1] - 1950] += -1

        sum = 0
        max_sum = 0 
        res = 0
        for x in range(0, len(sums)):
            sum += sums[x]
            if sum > max_sum:
                max_sum = sum
                res = 1950 + x
        
        return res

        print(sums) 


        pass


x = Solution()
print(x.maximumPopulation(logs = [[1950,1961],[1960,1971],[1970,1981]]))        
