from Tkinter import *
import janelaviewport as jvp
import translation as tran
import rotation as rot
import scale
import Queue

class Controller:
  """Manages transformations and control objects"""
  def __init__(self, paintzone):
    self.drawn_objects = []                       # List containing all drawned objects
    self.focused_objects = []                     # List of selected objects
  
  # The following transformations are applied to the focused objects
  def apply_translation(self):
    # Takes the first object as reference
    tran.Translation.apply(self.focused_objects, self.focused_objects)

  def register_object(self, objeto):
    list.append(self.drawn_objects, objeto)
  
  # def get_objects_in_range(self, 