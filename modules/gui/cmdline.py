from Tkinter import *
import re
from itertools import chain

class AutocompleteEntry(Entry):
  """Represents the graphic view of command line"""

  # List of words that will suggest autocomplete
  lista = [
    'create rectangle',
    'create triangle',
    'create square',
    'create line',
    'create circle',
    'select',
    'rotate',
    'translate',
    'scale',
    'resize']

  def __init__(self, parser, *args, **kwargs):
      Entry.__init__(self, *args, **kwargs)
      self.parser = parser
      # self.lista = AutocompleteEntry.lista        
      self.var = self["textvariable"]
      if self.var == '':
          self.var = self["textvariable"] = StringVar()

      self.var.trace('w', self.changed)
      self.bind("<Right>", self.selection)
      self.bind("<Up>", self.up)
      self.bind("<Down>", self.down)
      self.bind("<Return>", self.execute)

      self.lb_up = False
      self.pack(fill='both', side='bottom')
   
  def execute(self, event):
    self.parser.parse(self.var.get())

  def changed(self, name, index, mode):  
      if not self.var.get() == '':
        words = self.comparison()
        if words:            
            if not self.lb_up:
                self.lb = Listbox()
                self.lb.bind("<Double-Button-1>", self.selection)
                self.lb.bind("<Right>", self.selection)
                self.lb.place(x=self.winfo_x() + self.winfo_width(), y=self.winfo_y()-3*self.winfo_height())
                self.lb_up = True
            
            self.lb.delete(0, END)
            for w in words:
                self.lb.insert(END,w)
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
      return [w for w in self.lista if re.match(pattern, w)]

class CommandParser():
  """Represents a parser that will execute the commands"""
  def __init__(self, controller, drawer):
    self.controller = controller
    self.drawer = drawer
  
  # Simple command grammar
  commands = dict([
    ('create', [r'line <(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)> <(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)>',
                r'square <(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)> (\d+(?:\.\d+)?)',
                r'rectangle <(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)> <(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)>',
                r'triangle <(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)> <(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)> <(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)>',
                r'circle <(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)> (\d+(?:\.\d+)?)']),
    ('select',  r'<(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)> <(\d+(?:\.\d+)?),(\d+(?:\.\d+)?)>')])

  def parse(self, command):
    cmd = command.split(' ')[0]
    predicate = command.replace(cmd + ' ', '')
    expressions = self.commands.get(cmd)
    for exp in expressions:
      values = re.findall(exp, predicate)
      if not values == []:
        # Call draw functions
        if cmd == 'create':
          
          self.drawer.from_cmd_line(exp.split(' ')[0], list(chain.from_iterable(values)))


# if __name__ == '__main__':
#     root = Tk()

#     entry = AutocompleteEntry(lista, root)
#     entry.grid(row=0, column=0)
#     Button(text='nothing').grid(row=1, column=0)
#     Button(text='nothing').grid(row=2, column=0)
#     Button(text='nothing').grid(row=3, column=0)

#     root.mainloop()