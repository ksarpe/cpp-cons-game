import os

script_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(script_dir)

class PATHS:
    player_exe = os.path.join(parent_dir, 'bin', 'Debug-windows-x86_64', 'Player', 'Player.exe')
    # # TODO: remove player folder, because now we have only player without mediator
    map_file = os.path.join(parent_dir, 'mapa.txt')
    status_file = os.path.join(parent_dir, 'status.txt')
    commands_file = os.path.join(parent_dir, 'rozkazy.txt')