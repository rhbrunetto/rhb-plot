from Tkinter import *

class CheckBox():
  """Represents a CheckBox view"""
  def __init__(self, root, label, command, side='bottom'):
    var = IntVar()
    self._c = Checkbutton(
        root,
        text=label,
        variable=var,
        command=command)
    self._c.pack(fill=X, side=side)