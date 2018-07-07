import numpy as np

class Rotation():
  """Represents a rotation transfomation"""

  rotation_mask = []

  @staticmethod
  def apply(objeto, angle):
    return np.matmul(Rotation._generate_matrix(angle), objeto.matrix)

# TODO: Implementar a geracao da matriz
  @staticmethod
  def _generate_matrix(angle):
    return Rotation.rotation_mask
  