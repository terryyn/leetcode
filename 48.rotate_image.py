"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""

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
            
  
  # this is a general method for image rotate ---> reverse the list and swap
  # easy to figure out if drawing on sketch paper
