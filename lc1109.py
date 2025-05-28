class Solution:

    def corpFlightBookings(self, bookings, n: int):
        sums = [0] * (n + 1)

        for x in range(1, n + 1):
            sum = 0
            for bi in range(0, len(bookings)):
                b = bookings[bi]
                if x >= b[0] and x <= b[1]:
                    sum += b[2]
            sums[x] = sum

        return sums[1:]



    def corpFlightBookings2(self, bookings, n: int):
        sums = [0] * (n + 1)

        for bi in range(0, len(bookings)):
            b = bookings[bi]
            for x in range(b[0], b[1] + 1):
                sums[x] += b[2]

        return sums[1:]

x = Solution()
print(x.corpFlightBookings(bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5))
        
