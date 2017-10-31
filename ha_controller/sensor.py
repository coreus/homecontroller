from abc import ABCMeta, abstractmethod

class Sensor:
    __metaclass__ = ABCMeta

    def __init__(self,name=None,normalize=None):
        self.name = name
        self.normalize = 1
        if not normalize == None:
            self.normalize = normalize

    @abstractmethod
    def getState(self,entity):
        pass
    
    def normalization(self,value):
        return value / self.normalize

class Basic(Sensor):
    def getState(self,entity):
        return min(self.normalization(float(entity.state)),1)


class Binary(Sensor):
    def __init__(self, name=None,nullValue=None, *args, **kwargs):
        self.nullValue = 'off'
        if not self.nullValue == None:
            self.nullValue = nullValue
        super(Binary, self).__init__(*args, **kwargs)
    
    def getState(self,entity):
        if entity.state == self.nullValue :
            return 0
        return 1

class Sun(Sensor):
    def getState(self,entity):
        return (float(entity.attributes['elevation']) + 90) / 180