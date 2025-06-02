class Solution:
    def distributeCandies(self, n, limit):
        res = 0
        for i in range(0, limit + 1):
            if i > n:
                break
            new_n = n - i
            if new_n - limit > limit:
               continue 
            lower = new_n - limit if new_n - limit > 0 else 0
            upper = limit if new_n >= limit else new_n
            cnt =  upper - lower + 1
            print(cnt)
            res += cnt 

        return res


    def distributeCandies1(self, n, limit):
        combinations = []
        for i in range(0, limit + 1):
            for j in range(i, limit + 1):
                for k in range(j, limit + 1):
                    if i + j + k == n:
                        combinations.append((i, j, k))
        
        res = 0
        for i, j, k in combinations:
            denominatior = 1
            if i == k:
                denominatior = 6
            elif i == j or j == k:
                denominatior = 2
            else:
                denominatior = 1


            res += 6 // denominatior

        return res


    def distributeCandies2(self, n, limit):
        res = 0
        for i in range(0, limit + 1):
            for j in range(0, limit + 1):
                for k in range(0, limit + 1):
                    if i + j + k == n:
                        res += 1
        return res


x = Solution()
#print(x.distributeCandies(5, 2))
#print(x.distributeCandies2(5, 2))


print(x.distributeCandies(1, 3))
print(x.distributeCandies2(1,3))
