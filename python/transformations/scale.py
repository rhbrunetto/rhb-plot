import numpy as np

class Scale():
  """Represents a scale transfomation"""

  scale_mask = []

  @staticmethod
  def apply(objeto, xfactor, yfactor):
    return np.matmul(Scale._generate_matrix(xfactor, yfactor), objeto.matrix)

  @staticmethod
  def _generate_matrix(xfactor, yfactor):
    return Scale.scale_mask