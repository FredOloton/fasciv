class EntityActionLog():
    entity = None
    def __init__(self, entity):
        self.entity = entity

class Entity():
    dexterity = 0
    intelligence = 0
    strength = 0
    color = None
    logger = None

    def __init__(self):
        self.logger = EntityActionLog(self)
        return

    def displace(self):
        return
    
    def communicate(self,partner):
        self.intelligence += 1
        partner.intelligence += 1        
    
    def nourish(self):
        return