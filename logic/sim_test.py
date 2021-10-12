from entity import EntityFactory, EntityFactory, EntityGroup, Entity

def main():
    red_factory = EntityFactory(color="red")

    group_1 = EntityGroup()
    group_1.add_entities(red_factory.generate(amount=6, dexterity=3,intelligence=5, strength=7))


    black_factory = EntityFactory(color="black")

    group_2 = EntityGroup()
    group_2.add_entities(black_factory.generate(amount=4, dexterity=5,intelligence=3, strength=8))
    
    e1 = group_1.selectRandomMember()
    e2 = group_2.selectRandomMember()
    for x in range(0,3):
        e1.communicate(e2)

    print(group_1)
    print(group_2)
    # e1.logger.check_logs()

if __name__ == "__main__":
    main()