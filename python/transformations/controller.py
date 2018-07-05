from Tkinter import *
import janelaviewport as jvp
import translation as tran
import rotation as rot
import scale
import collections.deque as queue

class Controller:
  """Manages draws, transformations and update canvas"""
  def __init__(self, paintzone):
    self.drawn_objects = []                       # List containing all drawned objects
    self.focused_objects = []                     # List of selected objects
    self.paintzone = paintzone                    # Paintzone that will be managed
    self.function_queue = queue()           # Queue of functions (waiting for sufficient points)
  
  # The following transformations are applied to the focused objects



  def apply_translation(self):
    # Takes the first object as reference
    tran.Translation.apply(self.focused_objects, self.focused_objects)

  def clear_canvas(self):
    self.paintzone.clear()

  # def notify(self):
    

  def _enqueue_calling(self, function):
    self.function_queue.put(function)

  def _dequeue_calling(self, function):
    f = self.function_queue.get()
    f()

  def draw_line(self):
    if len(self.paintzone.buffer) < 2:
      self._enqueue_calling(self.draw_line)
      return
    self.paintzone.draw_line(list(sum(self.paintzone.buffer[:2], ())))
    self.paintzone.buffer = self.paintzone.buffer[2:]