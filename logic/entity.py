import random
from math import floor

# random 6 digit hex number generator
def six_hex_gen():
    #multiply hex by a random number
    #then strip it from it's hex marker and the first digit
    return str(hex(floor((1 + random.uniform(0, 1) ) * 0x1000000)))[3:]

class EntityActionLog():
    entity = None
    function_map = None
    log = []
    def __init__(self, entity):
        self.entity = entity
        self.function_map = {
            "displace": self.entity.displace,
            "communicate": self.entity.communicate,
            "nourish": self.entity.nourish,
            }
    
    def add_log(self,function_name, parameters):
        self.log.append(
            {
            "name": function_name,
            "paremeters": parameters,
            }
        )

    def check_logs(self):
        for i in range(len(self.log)):
            print(self.log[i])

class Entity():
    id = -1
    dexterity = 0
    intelligence = 0
    strength = 0
    color = None
    logger = None

    def __init__(self):
        self.id = six_hex_gen()
        self.logger = EntityActionLog(self)
        return

    def displace(self):
        self.logger.add_log("displace", None)
        return
    
    def communicate(self,partner):
        self.logger.add_log("communicate", None)
        self.intelligence += 1
        partner.intelligence += 1        
    
    def nourish(self):
        return