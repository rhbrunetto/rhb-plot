from Tkinter import *
from numpy import NINF as NINFINITE
from numpy import inf as INFINITE
from ..data.line import Line
from ..data.circle import Circle
from ..data.polygon import Polygon
from ..data.triangle import Triangle
from ..data.square import Square
from ..gui.popup import PopupWindow
from janelaviewport import JanelaViewport
from translation import Translation
from rotation import Rotation
from scale import Scale

class Controller:
  """Manages transformations and control objects"""
  def __init__(self, paintzone, topbar):
    self.drawn_objects = {}                       # Dictionary containing all drawned objects <ide, object>
    self.focused_objects = []                     # List of selected objects
    self.pz = paintzone                           # Paintzone object
    self.op = None                                # Current operation
    self.v_min = None                             # Drawn viewport minimun
    self.v_max = None                             # Drawn viewport maximum
    self.topbar = topbar                          # Topbar object
    self.disable_refresh = False                  # Disable Refresh

# Transformation Handle Functions

  def call_op_cmd(self, tname, tvalues):
    if tname == 'zoom-ext':
      self.disable_refresh = False
      self.normalize_window()
    elif tname == 'zoom':
      self.zoom(tvalues)
    else:
      self.disable_refresh = False
      T = self._transformation_names[tname]
      transf = T(*tvalues)
      for obj in self.focused_objects:
        transf.apply(obj)
      self.refresh_min_max(self.focused_objects)

  def zoom(self, tvalues):
    jv = JanelaViewport(
          tvalues[0], tvalues[1],
          self.pz.j_min, self.pz.j_max)
    jv.apply(self.drawn_objects.values())
    self.disable_refresh = True
    self.refresh_min_max(self.drawn_objects.values())

  def call_op(self, transformation):
    self.op = transformation
    if self.focused_objects == [] and not self.op == 'zoom':
      self.instruction("Select objects to apply transformation!")
      return
    if not self._check_requirements(self.op): return    
    T = self.get_args()
    if T == None: return
    for obj in self.focused_objects:
      T.apply(obj)
    self.refresh_min_max(self.focused_objects)
    self.instruction("Transformation (" + self.op + ") applied!")
  
  def instruction(self, message):
    """Displays a message on topbar"""
    self.topbar.simple_update(message)

  def cancel(self):
    """Cancels a function calling"""
    self.op = None

  def notify(self):
    """Called when a click is raised on canvas. Checks if some function needs to be called"""
    if self.op is None : return
    if self._check_requirements(self.op):
      self.call_op(self.op)
  
  # def _dequeue_calling(self):
  #   """Calls a function and keep focus if keepmode is enabled"""
  #   f = self.op
  #   T = self._transformation_names[tname]
  #     transf = T(*tvalues)
  #     for obj in self.focused_objects:
  #       transf.apply(obj)
  #     self.refresh_min_max(self.focused_objects)
  #   f()

  def _check_requirements(self, op):
    """Checks if focused function has sufficient points to be called"""
    if len(self.pz.buffer) < self._requirements.get(op): 
      self.instruction(
        "This transformation (" + self.op + ") needs " + str(self._requirements.get(op)) + " points (" + 
        str(self._requirements.get(op) - len(self.pz.buffer)) + " left)"
      )
      return False
    return True

  # The following transformations are applied to the focused objects
  # def apply_translation(self):
  #   """Applies a transformation in focused object list"""
  #   # Takes the first object as reference
  #   tran.Translation.apply(self.focused_objects, self.focused_objects)

  # def init_transformation(self, transformation):
  #     self.op = transformation()

  def delete(self, ides):
    """Deletes objects from drawn object list and from focused object list"""
    for single in ides:
      for w in self.drawn_objects.values():
        if w.ide == single:
          del self.drawn_objects[str(w.ide)]
      for x in self.focused_objects:
        if x.ide == single:
          self.focused_objects.remove(x)


  def select(self, ides, canvas):
    """Sets focus on selected objects"""
    for ide in ides:
      list.append(self.focused_objects, self.drawn_objects[str(ide)])
      try:
        canvas.itemconfig(ide, outline=self.pz.selection_color) # change color
      except:
        canvas.itemconfig(ide, fill=self.pz.selection_color) # change color
      self.pz.logger("> Selected object : " + str(ide))

  def unselect(self, ides, canvas):
    """Removes focus on selected objects"""
    for ide in ides:
      list.remove(self.focused_objects, self.drawn_objects[str(ide)])
      try:
        canvas.itemconfig(ide, outline=self.pz.color) # change color
      except:
        canvas.itemconfig(ide, fill=self.pz.color) # change color
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

    if self.disable_refresh : return
    if xmax > self.pz.j_max[0] or ymax > self.pz.j_max[1] or xmin < self.pz.j_min[0] or ymin < self.pz.j_min[1]:
       self.normalize_window()

  def normalize_window(self):
    """Applies a window-viewport transformation on all drawn objects and refreshes controller viewport coordinates"""
    if self.drawn_objects == {}: return
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

  # Maps a transformation command and its class
  _transformation_names = dict([
    ('translate', Translation),
    ('rotate', Rotation),
    ('scale', Scale),
    ('zoom', JanelaViewport)
  ])

  # Number of points required to apply an transformation
  _requirements = dict([
    ('translate', 0),
    ('rotate', 1),
    ('scale', 1),
    ('zoom', 2)
  ])

  def get_args(self):
    if self.op == None: return
    pts = self._requirements.get(self.op)                   # Get requirements

    if self.op == 'rotate':
      p = PopupWindow(self.pz.frame,
                      "Insira o angulo (em graus)")
      self.pz.frame.wait_window(p.top)
      p_list = list(sum(self.pz.buffer[:pts],  ()))
      T = Rotation(float(p.getval()), p_list[0], p_list[1])

    if self.op == 'scale':
      px = PopupWindow(self.pz.frame,
                      "Insira um fator para x")
      self.pz.frame.wait_window(px.top)
      py = PopupWindow(self.pz.frame,
                      "Insira um fator para y")
      self.pz.frame.wait_window(py.top)
      p_list = list(sum(self.pz.buffer[:pts],  ()))
      T = Scale(float(px.getval()), float(py.getval()),
                p_list[0], p_list[1])

    if self.op == 'translate':
      px = PopupWindow(self.pz.frame,
                      "Insira um offset para x")
      self.pz.frame.wait_window(px.top)
      py = PopupWindow(self.pz.frame,
                      "Insira um offset para y")
      self.pz.frame.wait_window(py.top)
      T = Translation(float(px.getval()), float(py.getval()))

    if self.op == 'zoom':
      self.zoom(self.pz.buffer[:pts])
      T = None

    self.pz.buffer = self.pz.buffer[pts:]                     # Remove points of buffer
    return T