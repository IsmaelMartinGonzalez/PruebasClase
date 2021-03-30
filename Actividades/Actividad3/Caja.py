from Actividades.Actividad3.Sobre import Sobre
from datetime import date, datetime


class Caja:
    # Atributes
    __id = -1
    __date = date
    __time = datetime
    __desc = ""
    __sobres = list()

    # Constructor
    def __init__(self, sobres, d):
        self.__id = self.__id + 2
        self.__date = date.today()
        self.__time = datetime.now()
        self.__desc = d
        self.__GenerarSobres(sobres)

    # Getters/Setters
    def getId(self):
        return self.__id

    def getDate(self):
        return self.__date

    def getTime(self):
        return self.__time

    def getDescription(self):
        return self.__desc

    def getSobres(self):
        return self.__sobres

    def SetId(self, Y):
        self.__id = Y

    def SetDate(self, Y):
        self.__date = Y

    def SetTime(self, Y):
        self.__time = Y

    def SetDescription(self, Y):
        self.__desc = Y

    # Other methods
    def __GenerarSobres(self, x):
        for i in range(x):
            self.getSobres().append(Sobre("Fallout", "Sobre del juego de mesa del aclamdo videojuego", 5))

    def verSobres(self):
        for i in self.getSobres():
            print(i.toString())

    def listarCartas(self):
        for s in self.getSobres():
           s.verCartas()
