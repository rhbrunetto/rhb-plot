import numpy as np

class Transformation(object):
  """Represents a generic transfomation"""
  def __init__(self, matrix):
    self.matrix = matrix          # Transformation matrix that will be applied

  def apply(self, objeto):
    """Applies the transformation in a object"""
    result = np.matmul(self.matrix, objeto.build_hmatrix())           # Multiply transformation matrix and object matrix (homogeneous coordinate)
    print self.matrix
    print objeto.matrix
    final_matrix = self.check_homogeneous(result)                     # Check the homogeneous coordinates (all must be zero) / normalizes matrix
    objeto.set_matrix(final_matrix)                                   # Apply changes to object
    print final_matrix

  def check_homogeneous(self, matrix):
    """Checks all homogeneous coordinates and, if necessary, normalizes the columns"""
    result = matrix
    res_lines = np.size(matrix, 0)
    max_w =  np.max(matrix[res_lines - 1])                                                          # Get biggest element in last row (homogeneous coordinate)
    if max_w > 1 :                                                                                  # If any homogeneous coordinate is bigger than 1, normalize matrix
      nmatrix = np.empty(shape=[res_lines,0])
      for i in range(np.size(matrix, 1)):                                                           # For each column
        nmatrix = np.append(nmatrix, np.divide(matrix[:,i],matrix[:,i][res_lines - 1]), axis=1)     # Divide columns by last row element
      result = nmatrix
    return result

  def generate_matrix(self, mask, filler_list):
    """Generates transformation matrix based on mask"""
    matrix = np.copy(mask)                             # Copies mask into a new matrix
    np.place(matrix, matrix>1, filler_list)            # Replaces any element bigger than 1 with next offset_list element
    return matrix