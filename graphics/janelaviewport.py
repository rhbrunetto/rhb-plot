import numpy as np

class JanelaViewport():
  """Represents a Window-Viewport transfomation"""

  janelaview_mask = []

  @staticmethod
  def apply(objetos):
    x_min = -1
    y_min = -1
    for obj in objetos:
      mmin = obj.matrix.min(axis=1)
      x_min = min(x_min, int(mmin[0][0]))
      y_min = min(y_min, int(mmin[1][0]))
    return x_min, y_min

  @staticmethod
  def _generate_matrix(point):
    return JanelaViewport.janelaview_mask