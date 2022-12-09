#!/bin/bash
def square_matrix_simple(matrix=[]):
  # Create a new empty matrix with the same size as the input matrix
  squared_matrix = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

  # Loop through each element in the input matrix
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      # Square the element and add it to the new matrix
      squared_matrix[i][j] = matrix[i][j] * matrix[i][j]

  # Return the new matrix
  return squared_matrix

