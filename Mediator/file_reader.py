from paths import PATHS


class FileReader:
    def read_map(self):
        with open(PATHS.map_file, 'r') as f:
            return f.read()
    
    def read_status(self):
        with open(PATHS.status_file, 'r') as f:
            return f.read()
    
    def read_commands(self):
        with open(PATHS.commands_file, 'r') as f:
            return f.read()