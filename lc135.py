class Solution:
    def candy(self, ratings):
        candies = [1] * len(ratings)
        print(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] += candies[i - 1]

        print(candies)
        
        for x in range(len(ratings) - 2, -1, -1):
            if ratings[x] > ratings[x + 1] and candies[x] <= candies[x + 1]: 
                candies[x] = max(candies[x], candies[x + 1] + 1)

        print(candies)
        return sum(candies)





x = Solution()
#print(x.candy([1,3,2,2,1]))

#print(x.candy([1,2,87,87,87,2,1]))


#print(x.candy([29,51,87,87,72,12]))


#print(x.candy([1,2,3,1,0]))


print(x.candy([1,6,10,8,7,3,2]))



