import numpy as np

class Objeto():
  """Represents a Graphic Object."""
  def __init__(self, ide, coordinates, objtype='object'):
    self.ide = ide
    self.matrix = np.asmatrix(coordinates).transpose()
    self.type = objtype

  def get_matrix(self):
    return self.matrix

  def build_hmatrix(self):
    """Builds the homogeneous matrix that represents the Object"""
    if self.matrix is None: return None
    linha = np.asmatrix(np.ones(np.size(self.matrix, 1)), dtype=int)
    return np.append(self.matrix, linha, axis=0)
  
  def get_points(self):
    """Returns the point sequence to be drawn"""
    return list(np.array(self.matrix.transpose()).reshape(-1,))

  def __repr__(self):
    return str(self.ide)