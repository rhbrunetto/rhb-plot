from Tkinter import *
import mouseindicator as mi

class PaintZone:
  """Represents a Paint Zone on graphic interface (canvas)"""
  
  def __init__(self, root, bgcolor, h, w, draw_color="#000000"):
    self.canvas = Canvas(root, bg=bgcolor, height=h, width=w)           # Canvas view instantiation
    self.canvas.pack(expand=True, fill='both', side='right')
    self._color = draw_color
    self._mouseindicator = None                                         # View that tracks cursor position
    self.buffer = []                                                    # Click buffer (stores click position)
    def click(event):                                                   # Bind click to canvas
      self.draw_point(event.x, event.y)
      list.append(self.buffer, (event.x, event.y))
    self.canvas.bind('<Button-1>', click)

  def set_mouseindicator(self, root):
    self._mouseindicator = mi.MouseIndicator(root)
    def mouseMove(event):
	    self._mouseindicator.update(str(int(self.canvas.canvasx(event.x))), str(int(self.canvas.canvasy(event.y))))
    self.canvas.bind('<Motion>',mouseMove)

  
  def draw_point(self, x, y):
    self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=self._color, outline="")

  def draw_line(self, coord):
    self.canvas.create_line(coord, fill=self._color, dash=(4,4))


  def clear(self):
    self.canvas.delete("all")