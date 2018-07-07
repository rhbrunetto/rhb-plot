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
    self.drawer = None                                                  # Drawer to notify clicks    
    def click(event):                                                   # Bind click to canvas
      list.append(self.buffer, (event.x, event.y))  # Appends the click position to buffer
      if self.drawer is not None:
        self.drawer.notify()                        # Notify drawer, if it has been setted
        if self.drawer.showPoint :
          self.draw_point(event.x, event.y)             # Draws the point on canvas
    self.canvas.bind('<Button-1>', click)

  def set_drawer(self, drawer):
    """Sets a drawer object, which is used to notify clicks on canvas"""
    self.drawer = drawer

  def set_mouseindicator(self, root):
    """Sets a view to receive the cursor position updates"""
    self._mouseindicator = mi.MouseIndicator(root)
    def mouseMove(event): 
	    self._mouseindicator.update(str(int(self.canvas.canvasx(event.x))), str(int(self.canvas.canvasy(event.y))))
    self.canvas.bind('<Motion>',mouseMove)

  # DRAW FUNCTIONS

  def draw_point(self, x, y):
    """Draws a point"""
    self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=self._color, outline="")

  def draw_line(self, coord):
    """Draws a line"""
    self.canvas.create_line(coord, fill=self._color, dash=(4,4))

  def draw_polygon(self, coord):
    """Draws a polygon"""
    self.canvas.create_polygon(coord, outline="RED", dash=(4,4))

  def draw_rectangle(self, coord):
    """Draws a rectangle"""
    self.canvas.create_polygon(coord, outline="RED", dash=(4,4))

  def draw_circle(self, coord):
    """Draws a cricle"""
    self.canvas.create_oval(coord, outline="RED", dash=(4,4))

  def find_to_me(self, window_coord):
    """Creates a window with specified coordinates and returns the id of overlapped items by the window"""
    return self.canvas.find_overlapping(x1 = window_coord[0],
                                        y1 = window_coord[1],
                                        x2 = window_coord[2],
                                        y2 = window_coord[3])

  def delete(self, items):
    """Clear from the canvas the selected items"""
    self.canvas.delete(items)

  def clear(self):
    """Clear the canvas"""
    self.canvas.delete("all")