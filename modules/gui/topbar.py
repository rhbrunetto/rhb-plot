from Tkinter import *

class TopBar:
  """Represents a top bar on canvas object"""
  def __init__(self, root, config, anchor='nw', side='top'):
    self._text = StringVar()
    self.config = config
    self.label = Label(root, textvariable=self._text, relief=FLAT)
    self.label.config(fg=config['normal_color'], bg=config['background'])
    self.label.pack(side='top', anchor='n', fill='both')

  def update(self, text, foreg, backg):
    self._text.set(text)
    self.label.config(fg=foreg, bg=backg)

  def simple_update(self, text):
    self._text.set(text)
    self.label.config(fg=self.config['normal_color'], bg=self.config['background'])