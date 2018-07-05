from Tkinter import *

class MenuButton():
  """Represents a Button on menu object"""
  def __init__(self, root, label, command):
    self.label = label
    self.command = command
    self._button = Button(root, text=label, command=command, wraplength=True)
    self._button.pack(fill=X)