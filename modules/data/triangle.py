import numpy as np
from objeto import Objeto

class Triangle(Objeto):
  """Represents a Triangle Object."""
  def __init__(self, ide, coordinates, options):
    Objeto.__init__(self, ide, coordinates, 'triangle')


  