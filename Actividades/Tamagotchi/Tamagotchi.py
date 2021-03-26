class Tamagotchi:
    # Atributes
    __nombre = ""
    __energia = 5
    __hambre = 0
    __estado = "content"

    # Constructor
    def __init__(self, n):
        self.__nombre = n

    # Getters/Setters
    def getNombre(self):
        return self.__nombre

    def getEnergia(self):
        return self.__energia

    def getHambre(self):
        return self.__hambre

    def getEstado(self):
        return self.__estado

    def setNombre(self,n):
        self.__nombre = n

    def setEnergia(self, e):
        self.__energia = e

    def setHambre(self,h):
        self.__hambre = h

    def setEstado(self,estado):
        self.__estado = estado

    # Definitions/Methods
    def comer(self, cantidad):
        if self.__estado == "famolenc":
            self.setHambre(self.__hambre-cantidad)
            self.setEstado("content")
            if self.__hambre <= 0:
                self.setHambre(0)
                return print("El " + self.getNombre() + " ya no tiene hambre")
            elif self.__hambre > 0:
                return print("El " + self.getNombre() + " sigue con hambre")

    def acariciar(self):
        print("Estado de " + self.getNombre() + " es " + self.getEstado()+". Energia: "+str(self.getEnergia())+". Hambre: "+str(self.getHambre()))
        self.setEstado("content")

    def jugar(self):
        if self.__energia <= 2 or self.__hambre >= 2:
            print(self.getNombre() + " no quiere jugar. Energia: " + str(self.getEnergia()) + " hambre: " + str(self.getHambre()))
        elif self.__estado == "content":
            self.setEnergia(self.__energia-1)
            self.setHambre(self.__hambre+1)
            self.setEstado("famolenc")
            print("Has jugado con " + self.getNombre())

    def dormir(self, horas):

        if self.__energia <= 2:
            self.setEnergia(self.__energia+horas)
            self.setEstado("famolenc")
            if self.__energia >= 5:
                self.setEnergia(5)
            return print(self.getNombre() + " a dormido")
        else:
            return print(self.getNombre() + " no ha dormido")


