from Actividades.Actividad3.Carta import Carta
from random import choice


class Sobre:
    # Atributes
    __id = -1
    __nombre = ""
    __desc = ""
    __price = 0
    __cartas = list()

    # Constructor
    def __init__(self, n, d, p):
        self.__id = self.__id + 2
        self.__nombre = n
        self.__desc = d
        self.__price = p

    # Getters/Setters
    def getID(self):
        return self.__id

    def getNombre(self):
        return self.__nombre

    def getDescription(self):
        return self.__desc

    def getPrice(self):
        return self.__price

    def getCartas(self):
        return self.__cartas

    def SetId(self, i):
        self.__id = i

    def SetNombre(self, n):
        self.__nombre = n

    def SetDescription(self, d):
        self.__desc = d

    def SetPrice(self, p):
        self.__price = p

    # Other methods

    def __generarCarta(self):
        nombre = ""
        Atk = 0
        defe = 0
        vida = 0
        passiv = ""
        rareza = choice(["Normal", "Rara", "Super rara", "Ultra rara", "Legendaria"])
        tipo = choice(["Tierra", "Aire", "Mar"])
        if rareza == "Normal":
            nombre = choice(["Iniciado", "Escriba", "Torreta Mk.I"])
            Atk = choice([1, 2, 3, 4, 5, 6])
            defe = choice([0, 2, 4, 6])
            vida = choice([1, 3, 5])
            if nombre == "Iniciado" or nombre == "Escriba":
                passiv = "Ganas de Combatir: +2 al ATK por cada Iniciado o Escriba en mesa"
            else:
                passiv = "Servicio implacable: La Torreta MK.I suma +2 al DEF si hay un Escriba en mesa o un +2 ATK " \
                         "si hay un Iniciado "
        elif rareza == "Rara" or rareza == "Super rara":
            nombre = choice(["Caballero", "Jefe de equipo", "Torreta Mk.II"])
            Atk = choice([7, 8, 9, 10, 11, 12])
            defe = choice([8, 10, 12, 14])
            vida = choice([7, 9, 11])
            if nombre == "Caballero" or nombre == "Jefe de equipo":
                passiv = "Bien Organizados: +2 al ATK a los Iniciados o Escribas en mesa por cada Caballero o Jefe de " \
                         "equipo "
            else:
                passiv = "Servicio implacable V.2: La Torreta MK.II suma +4 al DEF si hay un Jefe de equipo en mesa o " \
                         "un +4 ATK si hay un Caballero "
        elif rareza == "Ultra rara" or rareza == "Legendaria":
            nombre = choice(["Paladin", "Elder", "Securtron"])
            Atk = choice([13, 14, 15, 16, 17, 18])
            defe = choice([18, 20, 22, 24])
            vida = choice([13, 15, 17])
            if nombre == "Paladin" or nombre == "Elder":
                passiv = "AD Victoriam: Todos los iniciados y Caballeros ganan un +4 por cada Paladin o Elder en mesa"
            else:
                passiv = "Defensa mecanozada: Por cada torreta MK.I o MK.II en mesa el securitron suma un +1 a la " \
                         "DEF. Si es" \
                         "legendaria sumara un +2."
        a = Carta(nombre, tipo, rareza, Atk, defe, vida, passiv)
        self.getCartas().append(a)

    def verCartas(self):
        for i in range(5):
            self.__generarCarta()

        for i in self.getCartas():
            print(i.toString())

    def toString(self):
        return str(self.getID())+"\tPrecio:"+str(self.getPrice())+" Nombre:"+self.getNombre()+"\n"\
            +self.getDescription()+" Total de Cartas: "+str(len(self.getCartas()))
