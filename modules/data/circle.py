import numpy as np
from objeto import Objeto

class Circle(Objeto):
  """Represents a Circle Object."""
  def __init__(self, ide, coordinates, options):
    Objeto.__init__(self, ide, coordinates, 'circle')
    self.ray = options.get('ray')

  