# WAP that allows the user to obtain information about the file system. You must follow Software Development Process.

import os
import sys

class FileSystem:
    def __init__(self, path):
        self.path=path
        self.size=self.calculate_size()
        self.files=self.get_files()
        self.directories=self.get_directories()
    
    def calculate_size(self):
        return os.path.getsize(self.path)
    
    def get_files(self):
        return [f for f in os.listdir(self.path) if os.path.isfile(f)]
    
    def get_directories(self):
        return [d for d in os.listdir(self.path) if os.path.isdir(d)]
    
    def __str__(self):
        return f'{self.path} {self.size} {self.files} {self.directories}'
    
path=input('Enter the path: ')
if os.path:
    fs=FileSystem(path)
    print(fs)
else:
    sys.exit('Invalid path')

