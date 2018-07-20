import numpy as np
from transformation import Transformation

scale_mask = [[2, 0, 2],
              [0, 2, 2],
              [0, 0, 1.0]]

class Scale(Transformation):
  """Represents a scale transfomation"""

  def __init__(self, sx, sy, ref):
    self.sx = sx
    self.sy = sy
    self.ref = ref
    super(Scale, self).__init__(self.generate_matrix(scale_mask, [
      self.sx, self.ref[0]-self.ref[0]*self.sx,
      self.sy, self.ref[1]-self.ref[1]*self.sy]))