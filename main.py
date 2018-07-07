import sys
from modules.gui import paintzone
from modules.gui import sidebar
from modules.gui import menubutton
from modules.gui import window
from modules.gui import checkbox
from modules.graphics import controller as ctrl
from modules.graphics import drawer as drw
import argparse
import json
import os

# to be used if anything fails
# ! /usr/bin/python2.7
# -*- coding: UTF-8 -*-

def init_components(win, menuroot, pz):
  controller = ctrl.Controller(pz)                                                              # Controller to manage objects 
  drawer = drw.Drawer(pz, controller)                                                           # Controller to manage the canvas 
  pz.set_drawer(drawer)                                                                         # Set drawer to paintzone to notify clicks
  menubutton.MenuButton(menuroot, 'Line', lambda m=drawer.draw_line: drawer.call_function(m))   # Draw line button
  menubutton.MenuButton(menuroot, 'Triangle', lambda m=drawer.draw_triangle: drawer.call_function(m))   # Draw triangle button
  menubutton.MenuButton(menuroot, 'Circle', lambda m=drawer.draw_circle: drawer.call_function(m))   # Draw triangle button
  menubutton.MenuButton(menuroot, 'Rectangle', lambda m=drawer.draw_rectangle: drawer.call_function(m))   # Draw rectangle button
  menubutton.MenuButton(menuroot, 'Square', lambda m=drawer.draw_square: drawer.call_function(m))   # Draw square button
  menubutton.MenuButton(menuroot, 'Delete', lambda m=drawer.delete: drawer.call_function(m))   # Draw square button
  menubutton.MenuButton(menuroot, 'Close', win.stop, side='bottom')                             # Close button
  menubutton.MenuButton(menuroot, 'Clear', drawer.clear_canvas, side='bottom')                  # Clear button
  checkbox.CheckBox(menuroot, 'Keep Drawing', drawer.keep_drawing)                              # Checkbox to keep drawing
  checkbox.CheckBox(menuroot, 'Draw Clicks', drawer.toggle_point)                               # Checkbox to draw clicks
  # menubutton.MenuButton(menuroot, 'Translate', lambda event, pz.current : translation.Translation.apply)                    #Close button

def main(config):
  canvas_cfg    = config['canvas']
  side_cfg      = config['sidebar']
	
  win = window.Window()
	
  pz = paintzone.PaintZone(    
      win.root,
      str(canvas_cfg['background']),
      int(canvas_cfg['altura']),
      int(canvas_cfg['largura']),
      str(canvas_cfg['draw_color']))

  sb = sidebar.SideBar(
    win.root,
    str(side_cfg['background']),
    int(canvas_cfg['altura']),
    int(side_cfg['largura'])
  )
  
  pz.set_mouseindicator(sb.frame)

  init_components(win, sb.frame, pz)

  win.start()

if __name__ == '__main__':
  def configuration(path, argparse):
    """Loads a config file in path"""
    filepath = os.path.join(os.path.dirname(__file__), path)
    if os.path.exists(filepath):
        jsonfile = open(filepath)
        try:
            config = json.load(jsonfile)
            jsonfile.close()
            return config
        except Exception as e:
            message = ('Bad config file at "{}".').format(filepath)
            raise argparse.ArgumentError(message)
    else:
        message = ('Config file "{}" does\'t exists.').format(filepath)
        raise argparse.ArgumentError(message)
  
  """Load argument parser"""
  arguments_parser = argparse.ArgumentParser(
      prog=sys.argv[0],
      description='rhb-plot')
  arguments_parser.add_argument(
      '-c', '--config',
      nargs=1,
      metavar='<FILE>',
      default=configuration('config.json', argparse),
      type=configuration,
      help=('The rhb-plot configuration file. '
            'Default: "config.json"'))
  arguments = arguments_parser.parse_args(sys.argv[1:])
  main(arguments.config)
