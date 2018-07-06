from Tkinter import *
import Queue

class Drawer:
  """Manages draws and update canvas"""
  def __init__(self, paintzone):
    self.paintzone = paintzone                    # Paintzone that will be managed
    # self.function_queue = Queue.Queue()           # Queue of functions (waiting for sufficient points)
    self.current_function = None                  # Current function of draw (waiting for sufficient points)
    self.keepDrawing      = False                 # Set draw function as permanent (keeps calling)

  # Defines how many points each object needs to be drawn
  _requirements = dict([
    ('draw_line', 2),
    ('draw_circle', 2),
    ('draw_triangle', 3),
    ('draw_rectangle', 4),
    ('draw_square', 2)
  ])

# FUNCTION QUEUE HANDLERS

  def notify(self):
    """Called when a click is raised on canvas. Checks if some function needs to be called"""
    if self.current_function is None : return
    if self._check_requirements(self.current_function):
      self._dequeue_calling()
      
  def _enqueue_calling(self, function):
    """Sets focus to a function"""
    self.current_function = function

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

# DRAW FUNCTIONS

  def draw_line(self):
    """Draws a line"""
    if not self._check_requirements(self.draw_line):
      self._enqueue_calling(self.draw_line)
    else:
      if self.keepDrawing : self._enqueue_calling(self.draw_line)
      self.paintzone.draw_line(list(sum(self.paintzone.buffer[:2], ())))
      self.paintzone.buffer = self.paintzone.buffer[2:]

  def draw_triangle(self):
    """Draws a triangle"""
    if not self._check_requirements(self.draw_line):
      self._enqueue_calling(self.draw_line)
    else:
      if self.keepDrawing : self._enqueue_calling(self.draw_line)
      self.paintzone.draw_line(list(sum(self.paintzone.buffer[:2], ())))
      self.paintzone.buffer = self.paintzone.buffer[2:]

  def clear_canvas(self):
    """Clears the canvas, the paintzone point buffer and the focused function"""
    self.paintzone.clear()
    self.paintzone.buffer = []
    self.current_function = None