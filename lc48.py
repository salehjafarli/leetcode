class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        self.rotate_rec(matrix, 0, n)

    def rotate_rec(self, matrix, cor1, cor2):
        if cor1 >= cor2:
            return 

        for x in range(0, cor2 - cor1):
            self.matrix_swap(matrix, (cor2, cor2 - x), (cor1 + x, cor2))
            self.matrix_swap(matrix, (cor1 + x, cor2), (cor1, cor1 + x))
            self.matrix_swap(matrix, (cor1, cor1 + x), (cor2 - x, cor1))

        self.rotate_rec(matrix, cor1 + 1, cor2 - 1)


    def matrix_swap(self, matrix, t1, t2):
        matrix[t1[0]][t1[1]], matrix[t2[0]][t2[1]] = matrix[t2[0]][t2[1]], matrix[t1[0]][t1[1]]


    def printmat(self, matrix):
        for x in matrix:
            print(x)
        print()


s = Solution()

matrix = [[1,2],[3,4]]
s.printmat(matrix)
s.rotate(matrix)
s.printmat(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
s.printmat(matrix)
s.rotate(matrix)
s.printmat(matrix)

print()

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
s.printmat(matrix)
s.rotate(matrix)
s.printmat(matrix)