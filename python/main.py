import sys
from gui import paintzone
from gui import menubutton
from gui import window
import argparse
import json
import os


def init_components(win, menuroot):
  menubutton.MenuButton(menuroot, 'Close', win.stop)                    #Close button

def main(config):
  window_cfg = config['window']
	
  win = window.Window()
	
  pz = paintzone.PaintZone(    
      win.root,
      str(window_cfg['background']),
      int(window_cfg['altura']),
      int(window_cfg['largura']))
  
  sidebar = Frame(win.root, width=200, bg='white', height=500, relief='sunken', borderwidth=2)
  sidebar.pack(expand=True, fill='both', side='left', anchor='nw')

  init_components(win)

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
