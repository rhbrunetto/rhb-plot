from Tkinter import *

class MouseIndicator:
  """View that shows current cursor position on screen"""
  def __init__(self, root):
    self._text = StringVar()
    self.label = Label(root, textvariable=self._text, relief=FLAT)
    self.label.pack(side='bottom', anchor='sw', fill='both')

  def update(self, x, y):
    self._text.set('<' + x + ',' + y + '>')
