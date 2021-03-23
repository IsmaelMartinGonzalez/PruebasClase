# Atributes
s="Hola\n" \
  "salto\t tab"
# Definitions/Methods
print(s)
#loops
#Genera un bucle que se ejecuta tantas veces como la longitud de la palabra.
a="Ismael Holan"
for i in a:
    print(i)
#Tamaño de una palabra o de una cosa
print(len(a))
#Busca una palabra en concreto dentro de una variable
print("Hola" in a)
print("hola" not in a)
print("Hola" not in a)
#Imprime a partir de un rango
print(a[1:9])
#Transformar las letras
print(a.upper())
print(a.lower())
#Quitar espacio inicial
print(a.strip())
#Reemplazar letras por otras
print(a.replace("a","o"))
#Hacer de un string separado por espacios un array.
a="Hola Ismael Casa"
print(a.split(" "))
#Uso de variables
cantidad =3
item="Peras"
preci=22.8
txt="Quiero {} {} que cuesta {}€"
print(txt.format(cantidad,item,preci))
#Operadores
print("Hola"=="Hola")
#Control
x=5
y=4
if y<x:
    print(y)
elif x<y:
    print(x)
else:
    print("error")

#Inputs en variables
h=input("Pon algo: ")
print(h)