from Tkinter import *

class MenuButton():
  """Represents a Button on menu object"""
  def __init__(self, root, label, command, anchor='nw', side='top'):
    self.label = label
    self.command = command
    self._button = Button(root, text=label, command=command)
    self._button.pack(fill=X, anchor=anchor, side=side)