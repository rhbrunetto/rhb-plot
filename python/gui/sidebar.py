from Tkinter import *

class SideBar:
  """Represents a Side Bar on graphic interface (side menu)"""
  
  def __init__(self, root, bcolor, h, w):
    self.buttons = []
    self.frame = Frame(root, width=w, bg=bcolor, height=h, relief='sunken', borderwidth=2)
    self.frame.pack_propagate(False)    
    self.frame.pack(expand=False, fill='both', side='left', anchor='nw')