from Tkinter import *
# import Queue
from math import pow, sqrt

class Drawer:
  """Manages draws and update canvas"""
  def __init__(self, paintzone, controller):
    self.paintzone = paintzone                    # Paintzone that will be managed
    # self.function_queue = Queue.Queue()           # Queue of functions (waiting for sufficient points)
    self.current_function = None                  # Current function of draw (waiting for sufficient points)
    self.keepDrawing      = False                 # Set draw function as permanent (keeps calling)
    self.controller       = controller            # Set a Controller object, to store drawed objects
    self.showPoint        = False
    self.cmd_fn = {}
    self.initialize_dict()

  # Defines how many points each object needs to be drawn
  _requirements = dict([
    ('draw_line', 2),
    ('draw_circle', 2),
    ('draw_triangle', 3),
    ('draw_rectangle', 2),
    ('draw_square', 2),
    ('select', 2),
    ('unselect', 2),
    ('delete', 2),
    ('draw_square_bycommandline', 4)
  ])

# FUNCTION QUEUE HANDLERS

  def notify(self):
    """Called when a click is raised on canvas. Checks if some function needs to be called"""
    if self.current_function is None :
      self.controller.notify()
      return
    if self._check_requirements(self.current_function):
      self._dequeue_calling()
      
  def _enqueue_calling(self, function):
    """Sets focus to a function"""
    self.current_function = function
    self.controller.cancel()
  
  def cancel(self):
    """Cancels a function calling"""
    self.current_function = None

  def _dequeue_calling(self):
    """Calls a function and keep focus if keepmode is enabled"""
    f = self.current_function
    if not self.keepDrawing: self.current_function = None
    f()

  def _check_requirements(self, function):
    """Checks if focused function has sufficient points to be called"""
    if len(self.paintzone.buffer) < self._requirements.get(function.__name__): return False
    return True

  def keep_drawing(self):
    """Toggle keepmode and keeps (or not) executing function when notified"""
    if self.keepDrawing : self.current_function = None
    self.keepDrawing = not self.keepDrawing

  def toggle_point(self):
    """Toggle the point draw on click"""
    self.showPoint = not self.showPoint

# DRAW FUNCTIONS.
# Every function below uses the paintzone buffer points to draw their objects

  def call_function(self, function):
    """Manages draw functions calling"""
    if not self._check_requirements(function):
      self._enqueue_calling(function)
    else:
      if self.keepDrawing :
        self._enqueue_calling(function)
      function()

  def draw_line(self):
    """Draws a line"""
    pts = self._requirements.get(self.draw_line.__name__)                   # Get requirements
    ide = self.paintzone.draw_line(list(sum(self.paintzone.buffer[:pts], ())))    # Draw line on canvas
    self.controller.register_object(self.paintzone.buffer[:pts], ide, 'line')    # Register object on controller
    self.paintzone.buffer = self.paintzone.buffer[pts:]                     # Remove points of buffer

  def draw_triangle(self):
    """Draws a triangle"""
    pts = self._requirements.get(self.draw_triangle.__name__)                # Get requirements
    ide = self.paintzone.draw_polygon(list(sum(self.paintzone.buffer[:pts], ())))  # Draw triangle on canvas
    self.controller.register_object(self.paintzone.buffer[:pts], ide, 'triangle') # Register object on controller
    self.paintzone.buffer = self.paintzone.buffer[pts:]                      # Remove points of buffer

  def draw_rectangle(self):
    """Draws a rectangle"""
    pts = self._requirements.get(self.draw_rectangle.__name__)                      # Get requirements
    A = self.paintzone.buffer[0]
    C = self.paintzone.buffer[1]
    B = (A[0], C[1])
    D = (C[0], A[1])
    coords = [A,B,C,D]                             # Remove points of buffer
    ide = self.paintzone.draw_polygon(list(sum(coords, ()))) # Draw rectangle on canvas
    self.controller.register_object(coords, ide, 'rectangle')  # Register object on controller
    self.paintzone.buffer = self.paintzone.buffer[pts:]                             # Remove points of buffer


  def draw_circle(self):
    ''"""Draws a circle"""
    pts = self._requirements.get(self.draw_rectangle.__name__)                # Get requirements
    # TODO: Replace by lambda expression
    t1 = pow(self.paintzone.buffer[0][0] - self.paintzone.buffer[1][0], 2)
    t2 = pow(self.paintzone.buffer[0][1] - self.paintzone.buffer[1][1], 2)
    ray = sqrt(t1 + t2)
    coord = []
    coord.append(self.paintzone.buffer[0][0] + ray) #x1ray
    coord.append(self.paintzone.buffer[0][1] + ray) #y1ray
    coord.append(self.paintzone.buffer[0][0] - ray) #y2ray
    coord.append(self.paintzone.buffer[0][1] - ray) #y2ray
    ide = self.paintzone.draw_circle(coord)   # Draw circle on canvas
    self.controller.register_object(self.create_buffer_point(coord), ide, 'circle', dict([('ray', ray)])) # Register object on controller
    self.paintzone.buffer = self.paintzone.buffer[pts:]                                       # Remove points of buffer

  def draw_square(self):
    """Draws a square based on two points. Defines the side length based on largest variation on axis."""
    pts = self._requirements.get(self.draw_rectangle.__name__)                # Get requirements  
    # TODO: Replace by lambda expression
    xvar = abs(self.paintzone.buffer[1][0] - self.paintzone.buffer[0][0])
    yvar = abs(self.paintzone.buffer[1][1] - self.paintzone.buffer[0][1])

    if xvar > yvar: bigvar = xvar
    else : bigvar = yvar
    
    coord = [] 
    coord.append(self.paintzone.buffer[0][0])
    coord.append(self.paintzone.buffer[0][1])

    coord.append(self.paintzone.buffer[0][0] + bigvar) #x1ray
    coord.append(self.paintzone.buffer[0][1]) #y1ray

    coord.append(self.paintzone.buffer[0][0] + bigvar) #y2ray
    coord.append(self.paintzone.buffer[0][1] + bigvar) #y2ray

    coord.append(self.paintzone.buffer[0][0]) #y2ray
    coord.append(self.paintzone.buffer[0][1] + bigvar) #y2ray

    ide = self.paintzone.draw_polygon(coord)                                  # Draw square on canvas
    self.controller.register_object(self.create_buffer_point(coord), ide, 'square')                     # Register object on controller
    self.paintzone.buffer = self.paintzone.buffer[pts:]                       # Remove points of buffer
  
  def select(self):
    """Select (set focus on controller) items overlapped by a rectangle"""
    pts = self._requirements.get(self.select.__name__)                             # Get requirements      
    self.controller.select(                                                        # Get itens on the selected window
      self.paintzone.find_to_me(list(sum(self.paintzone.buffer[:pts], ()))),
      self.paintzone.canvas)
    self.paintzone.buffer = self.paintzone.buffer[pts:]                         # Remove points of buffer

  def unselect(self):
    """Unselect (remove focus on controller) items overlapped by a rectangle"""
    pts = self._requirements.get(self.select.__name__)                             # Get requirements      
    self.controller.unselect(                                                      # Get itens on the selected window
      self.paintzone.find_to_me(list(sum(self.paintzone.buffer[:pts], ()))),
      self.paintzone.canvas)
    self.paintzone.buffer = self.paintzone.buffer[pts:]                         # Remove points of buffer

  # def draw_square_bycommandline(self):
  def delete(self):
    """Delete items overlapped by a rectangle"""
    pts = self._requirements.get(self.delete.__name__)                          # Get requirements  
    ids = self.paintzone.find_to_me(list(sum(self.paintzone.buffer[:pts], ()))) # Get itens on the selected window
    self.controller.delete(ids)
    self.paintzone.delete(ids)
    self.paintzone.buffer = self.paintzone.buffer[pts:]                         # Remove points of buffer
    self.controller.refresh_min_max()

  def clear_canvas(self):
    """Clears the canvas, the paintzone point buffer and the focused function"""
    self.paintzone.clear()
    self.paintzone.buffer = []
    self.current_function = None
    self.controller.drawn_objects = {}
    self.controller.focused_objects = []
    self.controller.refresh_min_max()
  
# COMMAND LINE DRAW FUNCTIONS

  def draw_rectangle_cmd(self):
    # Converts values to tuples, buffers it and calls draw function
    self.paintzone.buffer = self.create_buffer_point(self.paintzone.buffer)
    return self.draw_rectangle()

  def draw_triangle_cmd(self):
    # Converts values to tuples, buffers it and calls draw function
    self.paintzone.buffer = self.create_buffer_point(self.paintzone.buffer)
    return self.draw_triangle()

  def draw_line_cmd(self):
    # Converts values to tuples, buffers it and calls draw function
    self.paintzone.buffer = self.create_buffer_point(self.paintzone.buffer)
    return self.draw_line()

  def select_cmd(self):
    # Converts values to tuples, buffers it and calls select function
    self.paintzone.buffer = self.create_buffer_point(self.paintzone.buffer)
    return self.select()

  def unselect_cmd(self):
    # Converts values to tuples, buffers it and calls unselect function
    self.paintzone.buffer = self.create_buffer_point(self.paintzone.buffer)
    return self.unselect()

  def draw_circle_cmd(self):
    # Requires center and radius
    start = tuple(self.paintzone.buffer[:2])
    p2 = (start[0] + self.paintzone.buffer[2], start[1] + self.paintzone.buffer[2])
    self.paintzone.buffer = [start, p2]
    return self.draw_circle()
    
  def draw_square_cmd(self):
    # Requires point and length
    start = tuple(self.paintzone.buffer[:2])
    p2 = (start[0] + self.paintzone.buffer[2], start[1] + self.paintzone.buffer[2])
    self.paintzone.buffer = [start, p2]
    return self.draw_square()

  def initialize_dict(self):
    """Initializes the name-function map used on command line"""
    self.cmd_fn['line'] = self.draw_line_cmd
    self.cmd_fn['circle'] = self.draw_circle_cmd
    self.cmd_fn['square'] = self.draw_square_cmd
    self.cmd_fn['triangle'] = self.draw_triangle_cmd
    self.cmd_fn['rectangle'] = self.draw_rectangle_cmd
    self.cmd_fn['select'] = self.select_cmd
    self.cmd_fn['unselect'] = self.unselect_cmd
    self.cmd_fn['clear'] = self.clear_canvas

  def from_cmd_line(self, command, values):
    """Handles the command and its values"""
    self.paintzone.buffer = map(int, values) if not values == None else []
    f = self.cmd_fn.get(command)
    return f()

  def create_buffer_point(self, coordinates):
    """Converts a sequence of values into a list of pairs"""
    def group(lst, n):
      for i in range(0, len(lst), n):
        val = lst[i:i+n]
        if len(val) == n:
          yield tuple(val)
    return list(group(coordinates, 2))