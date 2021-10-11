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
    dexterity = 0
    intelligence = 0
    strength = 0
    color = None
    logger = None

    def __init__(self):
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