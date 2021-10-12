from entity import EntityFactory, EntityFactory, EntityGroup, Entity

def main():
    redFactory = EntityFactory()
    
    group_1 = EntityGroup()
    group_1.add_entities(redFactory.generate(amount=6, dexterity=3,intelligence=5, strength=7))
    
    e1 = group_1.member_list[0]
    e2 = group_1.member_list[1]
    for x in range(0,3):
        e1.communicate(e2)

    for e in group_1.member_list:
        print(e)
    # e1.logger.check_logs()

if __name__ == "__main__":
    main()