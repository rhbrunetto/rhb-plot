import numpy as np
from transformation import Transformation

rotation_mask = [[2, 2, 2],
                 [2, 2, 2],
                 [0, 0, 1.0]]

class Rotation(Transformation):
  """Represents a rotation transfomation"""

  def __init__(self, theta, ref):
    self.theta =  theta * np.pi/180.0                 # Converts to radians
    self.cos = np.cos(self.theta)
    self.sin = np.sin(self.theta)
    self.ref = ref #(x, y)
    super(Rotation, self).__init__(self.generate_matrix(rotation_mask, [
      self.cos, (-1)*self.sin, self.ref[1]*self.sin - self.ref[0]*self.cos + self.ref[0],
      self.sin, self.cos,      (-1)*self.ref[0]*self.sin - self.ref[1]*self.cos + self.ref[1]]))