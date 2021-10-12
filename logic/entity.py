import random
from math import floor
from datetime import datetime


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
    def __init__(self, group = None, dexterity = 0, intelligence = 0, strength = 0, color = "grey"):
        self.id = hex_id_gen()
        self.group = group
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.strength = strength
        self.color= color
        self.logger = EntityActionLog(self)
        return

    def __str__(self):
        s = ("Entity#" + self.id 
        + "\n|  Dexterity: " + str(self.dexterity)
        + "\n|  Intelligence: " + str(self.intelligence)
        + "\n|  Strength: " + str(self.strength)
        + "\n|  Color: " + str(self.color)
        + "\n")
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

class EntityGroup:
    # contains the status between this group and other groups
    def __init__(self):
        self.id = hex_id_gen()        
        self.opinions = []
        self.member_list = []    
        self.mutation_factor = 0
        return
    
    def __str__(self):
        s = ("----------------------------\n Group#" + self.id + "\n")        
        for e in self.member_list:
            s += str(e)
        return s
    def add_entities(self, entities):
        for entity in entities:
            entity.group = self
            self.member_list.append(entity)

    def remove_entities(self, entities):
        for entity in entities:
            self.member_list.remove(entity)

    def selectRandomMember(self):
        return self.member_list[random.randrange(len(self.member_list) - 1)]

class EntityFactory:
    def __init__(self, color = "red"):
        self.color = color
        self.id = hex_id_gen()

    def generate(self, amount =1, dexterity = 0, intelligence = 0, strength = 0,):
        entities = []
        for i in range(amount):
            new_entity = Entity(dexterity = dexterity, intelligence = intelligence, strength = strength, color= self.color)
            entities.append(new_entity)
        return entities


class EntityActionLog():
    def __init__(self, entity):
        self.entity = entity
        self.function_map = {
            "displace": self.entity.displace,
            "communicate": self.entity.communicate,
            "nourish": self.entity.nourish,
            }
        
        self.log = []
    
    def add_log(self,function_name, parameters):
        self.log.append(
            {
            "name": function_name,
            "paremeters": parameters,
            "time": datetime.now()
            }
        )

    def check_logs(self):
        for i in range(len(self.log)):
            print(self.log[i])
