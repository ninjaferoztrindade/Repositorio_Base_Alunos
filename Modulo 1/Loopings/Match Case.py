import random
value = random.randint (0,2)
match value:
    case 0:
        print("Zero!")
    case 1:
        print("Um!")
    case _:
        print("Inesperado")    
