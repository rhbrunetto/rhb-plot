from Tkinter import *
from numpy import NINF as NINFINITE
from numpy import inf as INFINITE
import janelaviewport as jvp
import translation as tran
import rotation as rot
import scale
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
    self.op = None                                # Current operation
    self.v_min = None                             # Drawn viewport minimun
    self.v_max = None                             # Drawn viewport maximum

  def call_op_cmd(self, tname, tvalues):
    if tname == 'zoom-ext':
      self.normalize_window()
      return
    T = self._transformation_names[tname]
    transf = T(*tvalues)
    for obj in self.focused_objects:
      transf.apply(obj)
    self.refresh_min_max(self.focused_objects)

  def call_op(self, transformation):
    self.op = transformation
    if self.focused_objects == [] : return
    for obj in self.focused_objects:
      self.op.apply(obj)
      self._refresh_min_max(obj.get_points())
      self.pz.logger("> Transformation " + transformation.__name__ + " applied to object " + obj.ide)
    
  # The following transformations are applied to the focused objects
  # def apply_translation(self):
  #   """Applies a transformation in focused object list"""
  #   # Takes the first object as reference
  #   tran.Translation.apply(self.focused_objects, self.focused_objects)

  # def init_transformation(self, transformation):
  #     self.op = transformation()

  def select(self, ides, canvas):
    """Sets focus on selected objects"""
    for ide in ides:
      list.append(self.focused_objects, self.drawn_objects[str(ide)])
      canvas.itemconfig(ide, fill="blue") # change color
      self.pz.logger("> Selected object : " + str(ide))

  def unselect(self, ides, canvas):
    """Removes focus on selected objects"""
    for ide in ides:
      list.remove(self.focused_objects, self.drawn_objects[str(ide)])
      canvas.itemconfig(ide, fill="black") # change color
      self.pz.logger("> Unselected object : " + str(ide))

  def register_object(self, coordinates, ide, objtype, options=None):
    """Appends an object to the control list and refreshes controller viewport coordinates"""
    objclass = self._object_types.get(objtype)
    objeto = objclass(ide, coordinates, options)
    self.drawn_objects[str(ide)] = objeto
    self._refresh_min_max(list(sum(coordinates, ())))
    self.pz.logger("> New registered object : " + str(ide))


  def _refresh_min_max(self, coordinates):
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
      else:           # y
        if coordinates[i] < ymin: ymin = coordinates[i]
        if coordinates[i] > ymax: ymax = coordinates[i]
    
    self.v_max = (xmax, ymax)
    self.v_min = (xmin, ymin)

    if xmax > self.pz.j_max[0] or ymax > self.pz.j_max[1] or xmin < self.pz.j_min[0] or ymin < self.pz.j_min[1]:
       self.normalize_window()

  def normalize_window(self):
    """Applies a window-viewport transformation on all drawn objects and refreshes controller viewport coordinates"""
    if self.v_max == None or self.v_min == None: return
    deltay = abs(self.v_max[1] - self.v_min[1])
    deltax = abs(self.v_max[0] - self.v_min[0])
    percentage = 0.05                                                                       # Margin
    self.v_min = (self.v_min[0] - percentage*deltax, self.v_min[1] - percentage*deltay)     # Add a margin
    self.v_max = (self.v_max[0] + percentage*deltax, self.v_max[1] + percentage*deltay)     # Add a margin

    jv = JanelaViewport(self.v_min, self.v_max, self.pz.j_min, self.pz.j_max)               # Defines a window-viewport transformation
    jv.apply(self.drawn_objects.values())                                                   # Applies to drawn objects
    self.refresh_min_max(self.drawn_objects.values())
      
  def refresh_min_max(self, obj_list):
    """Refreshes all objects coordinates on screen and, if necessary, applies a window-viewport transformation"""
    self.v_max = self.v_min = None
    for obj in obj_list:                                                 # Refresh object coordinates in canvas
      self.pz.refresh_coordinates(obj.ide, obj.get_points())
    for obj in obj_list:                                                 # Refresh minimum and maximum values to current viewport
      self._refresh_min_max(obj.get_points())

  # Maps an object name and its class
  _object_types = dict([
    ('line', Line),
    ('square', Square),
    ('rectangle', Polygon),
    ('circle', Circle),
    ('triangle', Triangle)    
  ])

  # Maps an transformation command and its class
  _transformation_names = dict([
    ('translate', Translation),
    ('rotate', Rotation),
    ('scale', Scale),
  ])