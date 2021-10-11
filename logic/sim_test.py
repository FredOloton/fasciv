from entity import Entity

def main():
    e1 = Entity()
    e1.intelligence = 4
    e2 = Entity()    

    for x in range(0,3):
        e1.communicate(e2)
        print("e1: " + str(e1.intelligence))
        print("e2: " + str(e2.intelligence))

    e1.logger.check_logs()

if __name__ == "__main__":
    main()