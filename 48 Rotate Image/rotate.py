class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        matrix.reverse()
        length = len(matrix)
        for i in range(length):
            for j in range(i,length):
                temp = matrix[i][j] 
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
