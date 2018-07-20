import numpy as np
from transformation import Transformation

jvm_mask = [[2, 0, 2],
            [0, 2, 2],
            [0, 0, 1.0]]

class JanelaViewport(Transformation):
  """Represents a window-viewport transfomation"""
  
  def __init__(self, j_min, j_max, v_min, v_max):
    self.j_min = j_min    # j_min is the bottom-left point of window   (xmin, ymin)
    self.j_max = j_max    # j_max is the top-right point of window     (xmax, ymax)
    self.v_min = v_min    # v_min is the bottom-left point of viewport (umin, vmin)
    self.v_max = v_max    # v_max is the top-right point of viewport   (umax, vmax)
    self.Rw = (j_max[0] - j_min[0])/((j_max[1] - j_min[1]) * 1.0)
    self.Rv = (v_max[0] - v_min[0])/((v_max[1] - v_min[1]) * 1.0)
    
    if self.Rw > self.Rv:
      self.v_max = (self.v_max[0], ((v_max[0] - v_min[0])/self.Rw) + v_min[1])
    else:
      self.v_max = (self.Rw * (self.v_max[1] - self.v_min[1]) + self.v_min[0], self.v_max[1])

    #TODO: Centering

    self.sx = (self.v_max[0] - self.v_min[0])/((self.j_max[0] - self.j_min[0]) * 1.0)
    self.sy = (self.v_max[1] - self.v_min[1])/((self.j_max[1] - self.j_min[1]) * 1.0)

    super(JanelaViewport, self).__init__(self.generate_matrix(jvm_mask, [
      self.sx, self.sx*(-1)*self.j_min[0] + self.v_min[0],
      (-1)*self.sy, self.sy*(-1)*self.j_min[1] + self.v_min[1]]))
    
    print "JV MATRIX"
    print self.matrix
    
  def apply(self, objetos):
    return map(super(JanelaViewport, self).apply, objetos)