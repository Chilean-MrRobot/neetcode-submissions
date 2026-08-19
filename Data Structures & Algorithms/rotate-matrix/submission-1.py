class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        size = len(matrix)
        returnMatrix = [[] for i in range(size)]
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                returnMatrix[j].insert(0, value)

        print(returnMatrix)
        for i in range(len(matrix)):
            matrix[i] = returnMatrix[i]
        