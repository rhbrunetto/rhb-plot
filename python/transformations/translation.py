import numpy as np

class Translation():
  """Represents a translation transfomation"""

  translation_mask = []

  @staticmethod
  def apply(objeto, point):
    return np.matmul(Translation._generate_matrix(point), objeto.matrix)

  @staticmethod
  def _generate_matrix(point):
    return Translation.translation_mask