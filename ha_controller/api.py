import os,sys
sys.path.append('/usr/local/lib/python3.4/dist-packages/')
import homeassistant.remote as remote

class API:
    def __init__(self,ip=None):
        self.ip = '127.0.0.1'
        if(not ip is None):
            self.ip = ip
        
        self.resetStates()
    
    def refreshStates(self):
        self.api = remote.API(self.ip)
        self.__states =  remote.get_states(self.api)
        return self.__states
    
    def getStates(self):
        if(self.__states is None):
            return self.refreshStates()
        return self.__states
    
    def resetStates(self):
        self.__states = None

    def switchOn(self,entity_id):
        os.system('curl -X POST -H "Content-Type: application/json" -d \'{\"entity_id\": \"'+ entity_id + '\"}\' http://' + self.ip +':8123/api/services/switch/turn_on')
    
    def switchOff(self,entity_id):
        os.system('curl -X POST -H "Content-Type: application/json" -d \'{\"entity_id\": \"'+ entity_id + '\"}\' http://' + self.ip +':8123/api/services/switch/turn_off')