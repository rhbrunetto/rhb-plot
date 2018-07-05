from Tkinter import *

class SideBar:
  """Represents a Side Bar on graphic interface (side menu)"""
  
  def __init__(self, root, bgcolor, h, w):
    self.menus = []
    sidebar = tk.Frame(root, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
    sidebar.pack(expand=True, fill='both', side='left', anchor='nw')
    # arc = self.canvas.create_arc(coord, start=0, extent=150, fill="red")
    # coord = 10, 50, 240, 210

  def bindOnView(self):
    def mouseMove(event):
	    print self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
    self.canvas.bind('<Motion>',mouseMove)