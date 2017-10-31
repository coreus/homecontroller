from api import API
from config import Config


class neuralIO(API):

    def __init__(self,ip=None,input=None,output=None):
        self.input = self.initSensors(Config(input).read())
        self.output = self.initSensors(Config(output).read())
        super(neuralIO, self).__init__(ip = ip)
    
    def initSensors(self, config):
        module = __import__('sensor')
        for sensor in config:
            normalize = 1
            class_ = getattr(module, config[sensor]['type'])
            config[sensor]['object'] = class_()
            for attr in config[sensor]:
                if attr == 'group' or attr == 'type':
                    continue
                setattr(config[sensor]['object'],attr,config[sensor][attr])
        return config            

    def getInputStates(self):
        return self.getStates(self.input)
    
    def getOutputStates(self):
        return self.getStates(self.output)

    def getStates(self,io):
        entities = super(neuralIO, self).getStates()
        row = {}
        
        for entity in entities:
            if(entity.name in io.keys()):
                if not io[entity.name]['group'] in row :
                    row[io[entity.name]['group']]=0
                row[io[entity.name]['group']]+=io[entity.name]['object'].getState(entity)
                row[io[entity.name]['group']]= min(row[io[entity.name]['group']],1)
                
        return row