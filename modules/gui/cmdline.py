from Tkinter import *
import re
from itertools import chain

class AutocompleteEntry(Entry):
  """Represents the graphic view of command line"""

  # List of words that will suggest autocomplete
  lista = dict([
    (r'.*create line .*', 'create line <x1,y1> <x2,y2>'),
    (r'.*create square .*', 'create square <x1,y1> side_length'),
    (r'.*create rectangle .*', 'create rectangle <x1,y1> <x2,y2>'),
    (r'.*create triangle .*', 'create triangle <x1,y1> <x2,y2> <x3,y3>'),
    (r'.*create circle .*', 'create circle <x_center,y_center> radius'),
    (r'.*select .*', 'select <x1,y1> <x2,y2>'),
    (r'.*select all.*', 'select all'),
    (r'.*unselect .*', 'unselect <x1,y1> <x2,y2>'),
    (r'.*unselect all.*', 'unselect all'),
    (r'.*zoom .*', 'zoom <x1,y1> <x2,y2>'),
    (r'.*translate .*', 'translate <x_offset,y_offset>'),
    (r'.*rotate .*', 'rotate angle <x1,y1>'),
    (r'.*scale .*', 'scale sx sy <x1,y1>'),
    (r'.*clear all.*', 'clear all'),
    (r'.*zoom-ext.*', 'zoom-ext')])

  def __init__(self, parser, topbar, *args, **kwargs):
      Entry.__init__(self, *args, **kwargs)
      self.parser = parser
      self.var = self["textvariable"]
      if self.var == '':
          self.var = self["textvariable"] = StringVar()
      
      self.topbar = topbar
      self.var.trace('w', self.changed)
      self.bind("<Right>", self.selection)
      self.bind("<Up>", self.up)
      self.bind("<Down>", self.down)
      self.bind("<Return>", self.execute)
      self.lb_up = False
      self.pack(expand=True, fill='both', side='bottom')
      self.focus()
    
  def execute(self, event):
    success, msg = self.parser.parse(self.var.get())
    color = self.topbar.config['error_color']
    if success:
        self.var.set("")
        color = self.topbar.config['ok_color']
    self.topbar.update(msg, backg=color, foreg=self.topbar.config['background'])

  def changed(self, name, index, mode):  
      if not self.var.get() == '':
        words = self.comparison()
        if words:            
            if not self.lb_up:
                self.lb = Listbox(self.topbar.label.master, selectmode=SINGLE)
                self.lb.bind("<Double-Button-1>", self.selection)
                self.lb.bind("<Right>", self.selection)
                self.lb_up = True
                self.lb.place(
                  x=self.topbar.label.winfo_x(),
                  y=self.winfo_height()
                )
            
            self.lb.delete(0, END)
            for w in words:
                self.lb.insert(END,w)
                self.lb.config(width=0, height=0)
        else:
            if self.lb_up:
                self.lb.destroy()
                self.lb_up = False
      else:
        self.lb.destroy()
        self.lb_up = False
      
  def selection(self, event):
      if self.lb_up:
          self.var.set(self.lb.get(ACTIVE))
          self.lb.destroy()
          self.lb_up = False
          self.icursor(END)

  def up(self, event):
      if self.lb_up:
          if self.lb.curselection() == ():
              index = '0'
          else:
              index = self.lb.curselection()[0]
          if index != '0':                
              self.lb.selection_clear(first=index)
              index = str(int(index)-1)                
              self.lb.selection_set(first=index)
              self.lb.activate(index) 

  def down(self, event):
      if self.lb_up:
          if self.lb.curselection() == ():
              index = '0'
          else:
              index = self.lb.curselection()[0]
          if index != END:                        
              self.lb.selection_clear(first=index)
              index = str(int(index)+1)        
              self.lb.selection_set(first=index)
              self.lb.activate(index) 

  def comparison(self):
      pattern = re.compile('.*' + self.var.get() + '.*')
      sug = [self.lista[w] for w in self.lista if re.match(pattern, w)]
      if not sug == []: return sug
      return [self.lista[w] for w in self.lista if re.match(re.compile(w), self.var.get())]

class CommandParser():
  """Represents a parser that will execute the commands"""
  def __init__(self, controller, drawer):
    self.controller = controller
    self.drawer = drawer
  
  # Simple command grammar
  commands = dict([
    ('create', [r'line <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)> <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)>',
                r'square <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)> ([+-]?\d+(?:\.\d+)?)',
                r'rectangle <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)> <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)>',
                r'triangle <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)> <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)> <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)>',
                r'circle <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)> ([+-]?\d+(?:\.\d+)?)']),
    ('zoom',      [r'<([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)> <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)>']),
    ('select',    [r'<([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)> <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)>',
                   r'all']),
    ('unselect',  [r'<([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)> <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)>',
                   r'all']),
    ('translate', [r'<([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)>']),
    ('rotate',    [r'([+-]?\d+(?:\.\d+)?) <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)>']),
    ('scale',     [r'([+-]?\d+(?:\.\d+)?) ([+-]?\d+(?:\.\d+)?) <([+-]?\d+(?:\.\d+)?),([+-]?\d+(?:\.\d+)?)>']),
    ('clear',     [r'all']),
    ('zoom-ext',  [r'.*'])])

  def parse(self, command):
    """Parses an input, splitting and executing command"""
    cmd = command.split(' ')[0]
    predicate = command.replace(cmd + ' ', '')
    expressions = self.commands.get(cmd)
    if expressions == None: return False, "Wrong syntax!!!"
    for exp in expressions:
      values = re.findall(exp, predicate)
      if not values == []:
        if values == ['all']:
          val_list = [0,0,self.drawer.paintzone.j_max[0], self.drawer.paintzone.j_max[1]]
        else:
          val_list = list(chain.from_iterable(values))
        # Call drawer functions
        if cmd == 'create':
          self.drawer.from_cmd_line(exp.split(' ')[0], val_list)
          return True, "Object created!"
        if cmd == 'select':        
          self.drawer.from_cmd_line(cmd, val_list)
          return True, "Selected objects are in highlight!"
        if cmd == 'unselect':
          self.drawer.from_cmd_line(cmd, val_list)
          return True, "Objects beteween " + str(self.drawer.create_buffer_point(val_list)) + " had been unselected!"
        if cmd == 'clear':
          self.drawer.from_cmd_line(cmd, None)
          return True, "Canvas cleaned!"
        # Call controller functions
        if cmd == 'translate' or cmd == 'scale' or cmd == 'rotate' or cmd=='zoom-ext':
          try:
            self.controller.call_op_cmd(cmd, map(float, val_list))
          except:
            self.controller.call_op_cmd(cmd, None)
          return True, "Transformation applied: " + cmd + "!"
        if cmd == 'zoom':
          self.controller.call_op_cmd(cmd, self.drawer.create_buffer_point(map(float, val_list)))
          return True, "Transformation applied: " + cmd + "!"
        return False, "Wrong syntax!!!"
      # return False, "Wrong syntax!!!"



# if __name__ == '__main__':
#     root = Tk()

#     entry = AutocompleteEntry(lista, root)
#     entry.grid(row=0, column=0)
#     Button(text='nothing').grid(row=1, column=0)
#     Button(text='nothing').grid(row=2, column=0)
#     Button(text='nothing').grid(row=3, column=0)

#     root.mainloop()