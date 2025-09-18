def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Por favor, não utilize zeros!")
    except:
        print("\033[91m Algo deu errado...")                
    else:
        print(f"Seu resultado é: {result}")
    finally:
        print("\033[92m Vamos de novo? ")
divide(13,0)                
divide("a", 0)
divide("d", "e")
divide("-2","-777")
print("------x------")