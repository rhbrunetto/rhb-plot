from Tkinter import *
import Queue

class Drawer:
  """Manages draws and update canvas"""
  def __init__(self, paintzone):
    self.paintzone = paintzone                    # Paintzone that will be managed
    self.function_queue = Queue.Queue()           # Queue of functions (waiting for sufficient points)

  # Defines how many points each object needs to be drawn
  requirements = dict([
    ('draw_line', 2),
    ('draw_circle', 2),
    ('draw_triangle', 3),
    ('draw_rectangle', 4),
    ('draw_square', 2)
  ])

# FUNCTION QUEUE HANDLERS

  def notify(self):
    if self.function_queue.qsize() == 0 : return
    if self._check_requirements(list(self.function_queue.queue)[0]):
      self._dequeue_calling()
      
  def _enqueue_calling(self, function):
    self.function_queue.put(function)

  def _dequeue_calling(self):
    f = self.function_queue.get()
    f()

  def _check_requirements(self, function):
    if len(self.paintzone.buffer) < self.requirements.get(function.__name__): return False
    return True

# DRAW FUNCTIONS

  def draw_line(self):
    if not self._check_requirements(self.draw_line):
      self._enqueue_calling(self.draw_line)
    else:
      self.paintzone.draw_line(list(sum(self.paintzone.buffer[:2], ())))
      self.paintzone.buffer = self.paintzone.buffer[2:]

  def clear_canvas(self):
    self.paintzone.clear()