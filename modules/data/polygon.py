import numpy as np
from objeto import Objeto

class Polygon(Objeto):
  """Represents a Polygon Object."""
  def __init__(self, ide, coordinates, options):
    Objeto.__init__(self, ide, coordinates, 'polygon')


  