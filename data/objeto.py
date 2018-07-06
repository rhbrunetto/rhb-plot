import numpy as np

class Objeto():
  """Represents an Graphic Object."""
  def __init__(self):
    self.matrix = None

  def build_hmatrix(self):
    """Builds the homogeneous matrix that represents the Object"""
    if self.matrix is None: return None
    linha = np.asmatrix(np.ones(np.size(self.matrix, 1)))
    return np.append(self.matrix, linha, axis=0)
  