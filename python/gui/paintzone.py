from Tkinter import *

class PaintZone:
  """Represents a Paint Zone on graphic interface (canvas)"""
  
  def __init__(self, root, bgcolor, h, w):
    self.canvas = Canvas(root, bg=bgcolor, height=h, width=w)
    self.canvas.pack(expand=True, fill='both', side='right')
    # arc = self.canvas.create_arc(coord, start=0, extent=150, fill="red")
    # coord = 10, 50, 240, 210

  def bindOnView(self):
    def mouseMove(event):
	    print self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
    self.canvas.bind('<Motion>',mouseMove)