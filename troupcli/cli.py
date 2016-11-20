from argparse import ArgumentParser

from troup.node import NODE_LOCK_FILE_PATH


def sys_commands(cmd_parsers):
  parser = cmd_parsers.add_parser('sys', help='System commands')
  parser.add_argument('--list-nodes', action='store_true', help='List all known nodes on the system')
  parser.add_argument('--list-apps', action='store_true', help='List all known apps')
  

def app_commands(cmd_parsers):
  parser = cmd_parsers.add_parser('app', help='Applications commands')
  
  parser.add_argument('--add', dest='add_app_name', help='Add an app to the system', default='', metavar='APP')
  parser.add_argument('--desc', dest='app_desc', help='Application description', default='')
  parser.add_argument('--cmd', dest='app_cmd', help='Application cmd', default='')
  parser.add_argument('--req-cpu', dest='needs_cpu', help='Application CPU requirements', default=0)
  parser.add_argument('--req-mem', dest='needs_mem', help='Application memory requirements', default=0)
  parser.add_argument('--req-net', dest='needs_net', help='Application network requirements', default=0)
  parser.add_argument('--req-disk', dest='needs_disk', help='Application disk requirements', default=0)
  parser.add_argument('--param', dest='params', nargs='+', help='Extra parameters in the form: PARAM_NAME=PARAM_VALUE', default='')
  
  parser.add_argument('--update', dest='update_app_name', help='Update app info', default='', metavar='APP')
  
  parser.add_argument('--del', dest='delete_app_name', help='Delete an app', default='', metavar='APP')
  
  parser.add_argument('--show', dest='show_app_name', help='Show info about app', default='', metavar='APP')
  
  parser.add_argument('-r', '--run', dest='run_app_name', help='Run an app on the system', default='', metavar='APP')
  parser.add_argument('--forward-audio', dest='forward_audio', action='store_true', help='Whether to forward the audio from the host node where the app actually runs')
  parser.add_argument('--forward-video', dest='forward_video', action='store_true', help='Whether to forward the video from the host node where the app actually runs')
  parser.add_argument('--buffer-size', dest='buffer_size', help='Size of the buffer to capture from stdout. To disable use 0, to set to unlimited set -1', default=0)


def build_parser():
  parser = ArgumentParser(prog='troupcli')
  parser.add_argument('--lock-file', default=NODE_LOCK_FILE_PATH, help='Troup node lock file path')
  parser.add_argument('--nearest-node', default='', help='Full URL of the nearest node')
  
  cmd_parsers = parser.add_subparsers(title='commands', description='troupcli commands', dest='command', metavar='command')
  
  sys_commands(cmd_parsers)
  app_commands(cmd_parsers)
  
  return parser
  
  
  
if __name__ == '__main__':
  parser = build_parser()
  args = parser.parse_args()
  
