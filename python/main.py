import Tkinter
import tkMessageBox

top = Tkinter.Tk()

C = Tkinter.Canvas(top, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()
top.mainloop()

# !/usr/bin/python3.5
# import pysettings
# import pyforms
# from   pyforms          import BaseWidget
# from   pyforms.controls import ControlText
# from   pyforms.controls import ControlButton

# class SimpleExample1(BaseWidget):

#     def __init__(self):
#         super(SimpleExample1,self).__init__('Simple example 1')

#         #Definition of the forms fields
#         self._firstname     = ControlText('First name', 'Default value')
#         self._middlename    = ControlText('Middle name')
#         self._lastname      = ControlText('Lastname name')
#         self._fullname      = ControlText('Full name')
#         self._button        = ControlButton('Press this button')


# #Execute the application
# if __name__ == "__main__":   pyforms.start_app( SimpleExample1 )