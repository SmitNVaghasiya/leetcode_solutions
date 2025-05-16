class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rotated = []
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            rotated.append(temp)
        return rotated