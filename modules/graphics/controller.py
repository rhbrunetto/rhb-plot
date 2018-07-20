from Tkinter import *
from numpy import NINF as NINFINITE
from numpy import inf as INFINITE
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
from janelaviewport import JanelaViewport
from translation import Translation
from rotation import Rotation
from scale import Scale

class Controller:
  """Manages transformations and control objects"""
  def __init__(self, paintzone):
    self.drawn_objects = {}                       # Dictionary containing all drawned objects <ide, object>
    self.focused_objects = []                     # List of selected objects
    self.pz = paintzone                           # Paintzone object
    self.v_min = None                             # Drawn viewport minimun
    self.v_max = None                             # Drawn viewport maximum
  
  # The following transformations are applied to the focused objects
  def apply_translation(self, transformation):
    """Applies a transformation in focused object list"""
    # Takes the first object as reference
    tran.Translation.apply(self.focused_objects, self.focused_objects)

  def select(self, ides, canvas):
    """Sets focus on selected objects"""
    for ide in ides:
      list.append(self.focused_objects, self.drawn_objects[str(ide)])
      canvas.itemconfig(ide, fill="blue") # change color
    print self.focused_objects

  def unselect(self, ides, canvas):
    """Removes focus on selected objects"""
    for ide in ides:
      list.remove(self.focused_objects, self.drawn_objects[str(ide)])
      canvas.itemconfig(ide, fill="black") # change color
    print self.focused_objects

  def register_object(self, coordinates, ide, objtype, options=None):
    """Appends an object to the control list and refreshes controller viewport coordinates"""
    objclass = self._object_types.get(objtype)
    objeto = objclass(ide, coordinates, options)
    print coordinates
    self.drawn_objects[str(ide)] = objeto
    print self.drawn_objects
    self.refresh_min_max(list(sum(coordinates, ())))
    # print self.drawn_objects

  def refresh_min_max(self, coordinates):
    """Refreshes minimum and maximum values of controller viewport based on drawn object coordinates.
       If necessary, applies window-viewport transformation"""
    if self.v_max == None or self.v_min == None:
      xmin = ymin = INFINITE
      xmax = ymax = NINFINITE
    else:
      xmin = self.v_min[0]
      xmax = self.v_max[0]
      ymin = self.v_min[1]
      ymax = self.v_max[1]
    for i in range(len(coordinates)):
      if i % 2 == 0:  # x
        if coordinates[i] < xmin: xmin = coordinates[i]
        if coordinates[i] > xmax: xmax = coordinates[i]
      else:
        if coordinates[i] < ymin: ymin = coordinates[i]
        if coordinates[i] > ymax: ymax = coordinates[i]
    # xmin = min(lis,key=lambda item:item[0])[0]
    # xmax = max(lis,key=lambda item:item[0])[0]
    # ymin = min(lis,key=lambda item:item[1])[1]
    # ymax = min(lis,key=lambda item:item[1])[1]

    self.v_max = (xmax, ymax)
    self.v_min = (xmin, ymin)

    print self.v_max
    print self.v_min

    if xmax > self.pz.j_max[0] or ymax > self.pz.j_max[1] or xmin < self.pz.j_min[0] or ymin < self.pz.j_min[1]:
       self.normalize_window()

  def normalize_window(self):
    """Applies a window-viewport transformation on all drawn objects and refreshes controller viewport coordinates"""
    jv = JanelaViewport(self.v_min, self.v_max,
                        self.pz.j_min, self.pz.j_max)

    jv.apply(self.drawn_objects.values())
    print "Applied"
    self.v_max = None
    self.v_min = None
    for obj in self.drawn_objects.values():
      # self.refresh_min_max(obj.get_points())
      self.pz.refresh_coordinates(obj.ide, obj.get_points())

  # Maps an object name and its class
  _object_types = dict([
    ('line', Line),
    ('square', Square),
    ('rectangle', Polygon),
    ('circle', Circle),
    ('triangle', Triangle)    
  ])