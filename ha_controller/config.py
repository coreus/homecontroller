import os.path
import yaml

class Config:

    def __init__(self,file=None):
        self.file = file
        self._content = None


    def read(self):
        if not self._content == None :
            return self._content
        
        if not os.path.isfile(self.file) :
            return False

        with open(self.file, 'r') as stream:
            try:
                self._content = yaml.load(stream)
            except yaml.YAMLError as exc:
                return False
        return self._content
