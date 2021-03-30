class Carta:
    # Atributes
    __nombre=""
    __tipo=""
    __rareza=""
    __atk=0
    __defe=0
    __vida=0
    __passiv=""

    # Constructor
    def __init__(self,n,t,r,a,d,v,p):
        self.__nombre = n
        self.__tipo = t
        self.__rareza = r
        self.__atk = a
        self.__defe = d
        self.__vida = v
        self.__passiv = p

    # Getters/Setters
    def getNombre(self):
        return self.__nombre

    def getTipo(self):
        return self.__tipo

    def getRareza(self):
        return self.__rareza

    def getAtaque(self):
        return self.__atk

    def getDefensa(self):
        return self.__defe

    def getVida(self):
        return self.__vida

    def getPasiva(self):
        return self.__passiv

    def setNombre(self, n):
        self.__nombre = n

    def setNombre(self, t):
        self.__tipo = t

    def setNombre(self, r):
        self.__rareza = r

    def setNombre(self, a):
        self.__atk = a

    def setNombre(self, d):
        self.__defe = d

    def setNombre(self, v):
        self.__vida = v

    def setNombre(self, p):
        self.__passiv = p

    # Other methods
    def toString(self):
        return self.getNombre()+" Tipo:"+self.getTipo()+" Rareza:"+self.getRareza()+"\n"\
            "Ataque: "+str(self.getAtaque())+" Defensa:"+str(self.getDefensa())+" Vida:"+str(self.getVida())+"\n"\
            +self.getPasiva()+"\n"
