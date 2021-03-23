# Atributes
x="Ismael"
# Definitions/Methods
def miNombre(): #Definimos un metodo con variables de entrono
    x="Soy una Variable de entorno"
    print(x)
def miNombre2(): #Definimos un metodo que machaca la variable global
    global x
    x="Ya no soy Ismael"
    print(x)
miNombre()
print(x)
miNombre2()
print(x+" / Esta variable ha sido cambiada")
print("Soy de tipo: "+str(type(x)))#Nos muestra el tipo de variable y ademas casteamos para poder poner String