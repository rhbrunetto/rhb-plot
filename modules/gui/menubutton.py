from Tkinter import *

class MenuButton():
  """Represents a Button on menu object"""
  def __init__(self, root, label, command, anchor='nw', side='top', bgcolor='#ECECEC'):
    self.label = label
    self.command = command
    self._button = Button(root, text=label, command=command, bg=bgcolor)
    self._button.pack(fill=X, anchor=anchor, side=side)