from Tkinter import *

class Window:
  """Represents a Window that manages graphic interface components"""
  
  def __init__(self):
    self.root = Tk()
    self.root.resizable(width=False, height=False)

  def start(self):
    self.root.mainloop()

  def stop(self):
    self.root.destroy()

