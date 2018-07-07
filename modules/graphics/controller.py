from Tkinter import *
import janelaviewport as jvp
import translation as tran
import rotation as rot
import scale
import Queue
from ..data.line import Line
from ..data.circle import Circle
from ..data.polygon import Polygon
from ..data.triangle import Triangle
from ..data.square import Square

class Controller:
  """Manages transformations and control objects"""
  def __init__(self, paintzone):
    self.drawn_objects = []                       # List containing all drawned objects
    self.focused_objects = []                     # List of selected objects
  
  # The following transformations are applied to the focused objects
  def apply_translation(self):
    # Takes the first object as reference
    tran.Translation.apply(self.focused_objects, self.focused_objects)

  def register_object(self, coordinates, ide, objtype, options=None):
    objclass = self._object_types.get(objtype)
    objeto = objclass(coordinates, ide, options)
    list.append(self.drawn_objects, objeto)
    # print self.drawn_objects

  _object_types = dict([
    ('line', Line),
    ('square', Square),
    ('rectangle', Polygon),
    ('circle', Circle),
    ('triangle', Triangle)    
  ])