import numpy as np
from objeto import Objeto

class Line(Objeto):
  """Represents a Line Object."""
  def __init__(self, ide, coordinates, options):
    Objeto.__init__(self, ide, coordinates, 'line')


  