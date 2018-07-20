import numpy as np
from transformation import Transformation

translation_mask = [[1.0, 0, 2],
                    [0, 1.0, 2],
                    [0, 0, 1.0]]

class Translation(Transformation):
  """Represents a translation transfomation"""

  def __init__(self, dx, dy):
    self.dx = dx
    self.dy = dy
    super(Translation, self).__init__(self.generate_matrix(translation_mask, [self.dx, self.dy]))