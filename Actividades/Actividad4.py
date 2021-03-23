import random
# Atributes
numRandom=0
numUsuario=0
# Definitions/Methods
def start():
    global numUsuario
    global numRandom
    numRandom=random.randint(0, 10)
    print("Se ha generado un numero aleatorio(0-10) intenta adivinarlo")
    numUsuario=input("opcion-> ")
    if(numUsuario==numRandom):
        print("Lo has adivinado")
    else:
        print("No lo has ha adivinado. Adios!")
start()