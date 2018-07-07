import numpy as np
from objeto import Objeto

class Square(Objeto):
  """Represents a Square Object."""
  def __init__(self, ide, coordinates, options):
    Objeto.__init__(self, ide, coordinates, 'square')


  