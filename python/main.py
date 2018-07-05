import sys
from gui import paintzone
from gui import sidebar
from gui import menubutton
from gui import window
from transformations import controller as ctrl
import argparse
import json
import os


def init_components(win, menuroot, pz):
  controller = ctrl.Controller(pz)                                      # Controller to manage the canvas 
  menubutton.MenuButton(menuroot, 'Line', controller.draw_line)         # Close button
  menubutton.MenuButton(menuroot, 'Close', win.stop)                    # Close button
  # menubutton.MenuButton(menuroot, 'Translate', lambda event, pz.current : translation.Translation.apply)                    #Close button

def main(config):
  canvas_cfg = config['canvas']
	
  win = window.Window()
	
  pz = paintzone.PaintZone(    
      win.root,
      str(canvas_cfg['background']),
      int(canvas_cfg['altura']),
      int(canvas_cfg['largura']),
      str(canvas_cfg['draw_color']))

  sb = sidebar.SideBar(
    win.root,
    int(canvas_cfg['altura'])
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
