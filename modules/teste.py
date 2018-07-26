# # from Tkinter import Tk, Canvas

# # def callback(event):
# #     draw(event.x, event.y)

# # def draw(x, y):
# #     paint.coords(circle, x-20, y-20, x+20, y+20)

# # root = Tk()
# # paint = Canvas(root)
# # paint.bind('<Motion>', callback)
# # paint.pack()

# # circle = paint.create_oval(0, 0, 0, 0)
# # root.mainloop()
# from Tkinter import *
# import re

# lista = ['a', 'actions', 'additional', 'also', 'an', 'and', 'angle', 'are', 'as', 'be', 'bind', 'bracket', 'brackets', 'button', 'can', 'cases', 'configure', 'course', 'detail', 'enter', 'event', 'events', 'example', 'field', 'fields', 'for', 'give', 'important', 'in', 'information', 'is', 'it', 'just', 'key', 'keyboard', 'kind', 'leave', 'left', 'like', 'manager', 'many', 'match', 'modifier', 'most', 'of', 'or', 'others', 'out', 'part', 'simplify', 'space', 'specifier', 'specifies', 'string;', 'that', 'the', 'there', 'to', 'type', 'unless', 'use', 'used', 'user', 'various', 'ways', 'we', 'window', 'wish', 'you']


# class AutocompleteEntry(Entry):
#     def __init__(self, lista, *args, **kwargs):
#         Entry.__init__(self, *args, **kwargs)
#         self.lista = lista        
#         self.var = self["textvariable"]
#         if self.var == '':
#             self.var = self["textvariable"] = StringVar()

#         self.var.trace('w', self.changed)
#         self.bind("<Right>", self.selection)
#         self.bind("<Up>", self.up)
#         self.bind("<Down>", self.down)
        
#         self.lb_up = False

#     def changed(self, name, index, mode):  

#         if self.var.get() == '':
#             self.lb.destroy()
#             self.lb_up = False
#         else:
#             words = self.comparison()
#             if words:            
#                 if not self.lb_up:
#                     self.lb = Listbox()
#                     self.lb.bind("<Double-Button-1>", self.selection)
#                     self.lb.bind("<Right>", self.selection)
#                     self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
#                     self.lb_up = True
                
#                 self.lb.delete(0, END)
#                 for w in words:
#                     self.lb.insert(END,w)
#             else:
#                 if self.lb_up:
#                     self.lb.destroy()
#                     self.lb_up = False
        
#     def selection(self, event):

#         if self.lb_up:
#             self.var.set(self.lb.get(ACTIVE))
#             self.lb.destroy()
#             self.lb_up = False
#             self.icursor(END)

#     def up(self, event):

#         if self.lb_up:
#             if self.lb.curselection() == ():
#                 index = '0'
#             else:
#                 index = self.lb.curselection()[0]
#             if index != '0':                
#                 self.lb.selection_clear(first=index)
#                 index = str(int(index)-1)                
#                 self.lb.selection_set(first=index)
#                 self.lb.activate(index) 

#     def down(self, event):

#         if self.lb_up:
#             if self.lb.curselection() == ():
#                 index = '0'
#             else:
#                 index = self.lb.curselection()[0]
#             if index != END:                        
#                 self.lb.selection_clear(first=index)
#                 index = str(int(index)+1)        
#                 self.lb.selection_set(first=index)
#                 self.lb.activate(index) 

#     def comparison(self):
#         pattern = re.compile('.*' + self.var.get() + '.*')
#         return [w for w in self.lista if re.match(pattern, w)]

# if __name__ == '__main__':
#     root = Tk()

#     entry = AutocompleteEntry(lista, root)
#     entry.grid(row=0, column=0)
#     Button(text='nothing').grid(row=1, column=0)
#     Button(text='nothing').grid(row=2, column=0)
#     Button(text='nothing').grid(row=3, column=0)

#     root.mainloop()

# import numpy as np
# from graphics.janelaviewport import JanelaViewport as JV
# from data.objeto import Objeto as O

# o = O(0, [(2, 1),
#           (4, 4),
#           (4, 2),
#           (3, 1),
#           (1, 1)], 'rectangle')

# jmin = (0,0)
# jmax = (4,3)
# vmin = (0,0)
# vmax = (1,1)

# jv = JV(jmin, jmax, vmin, vmax)

# jv.apply([o])


from Tkinter import *

class Test(Frame):
    def __init__(self, master=None):
	Frame.__init__(self, master)
	Pack.config(self)
	self.createWidgets()

    def action_(self):
        print "action"
        self.plot.coords(self.line,10,0,10,10,80,100,100,200)

    def action(self):
        print "action2, This one fails:"
        liste=[10,0,10,10,80,100,100,200]
        self.plot.coords(self.line,liste)

    def createWidgets(self):
	self.QUIT = Button(self, text='QUIT', foreground='red',
			   command=self.quit)

	self.Action = Button(self, text='Action', foreground='red',
			   command=self.action_)
        self.plot=Canvas(self, width="5i", height="5i")
        liste=[0,0,10,10,80,150,200,200]
        self.line=self.plot.create_line(liste)

	self.plot.pack(side=TOP)
	self.QUIT.pack(side=LEFT, fill=BOTH)
	self.Action.pack(side=LEFT, fill=BOTH)

test = Test()
test.mainloop()