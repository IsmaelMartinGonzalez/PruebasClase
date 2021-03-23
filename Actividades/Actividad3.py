from random import randint

# Atributes
nombre = ""
random = 0


# Definitions/Methods
def nombreRandom():
    global nombre
    global random
    nombre = input("Introduce tu nombre: ")
    random = randint(0, 10)
    for i in range(random):
        print(nombre)


nombreRandom()
