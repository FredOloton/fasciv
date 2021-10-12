import random
from math import floor

# random hex number generator
def hex_id_gen(digit_amount = 10):
    # though this object is being held in the datatype
    # what we actually make use of is it's hex representation
    base_hex_number = int("0x1" + digit_amount *("0"),16)
    # base_hex_number = 0x100000000000
    random_number = (1 + random.uniform(0, 1))
    #multiply hex by a random number
    #then strip it from it's hex prefix and the first digit
    return str(hex(floor(random_number * base_hex_number)))[3:]

class Entity():
    id = None
    dexterity = 0
    intelligence = 0
    strength = 0
    color = None
    logger = None

    def __init__(self):
        self.id = hex_id_gen()
        self.logger = EntityActionLog(self)
        return

    def __str__(self):
        s = ("Entity#" + self.id 
        + "\n|  Dexterity: " + str(self.dexterity)
        + "\n|  Intelligence: " + str(self.intelligence)
        + "\n|  Strength: " + str(self.strength)
        + "\n|  Color: " + str(self.color))
        return s

    def displace(self):
        self.logger.add_log("displace", None)
        return
    
    def communicate(self,partner):  
        self.logger.add_log("communicate", None)
        self.intelligence += 1
        partner.intelligence += 1        
    
    def nourish(self):
        return

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

class EntitGroup:
    member_id_list = []
    def __init__(self):
        pass