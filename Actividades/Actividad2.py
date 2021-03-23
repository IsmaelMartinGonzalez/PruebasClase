# Atributes
num1=0
num2=0
exit=False
# Definitions/Methods
def suma(n1,n2):
    return n1+n2
def resta(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def switch(op):
    if op=="A":
        return print(suma(num1,num2))
    if op=="B":
        return print(resta(num1,num2))
    if op=="C":
        return print(mult(num1,num2))
    if op=="D":
        return print(div(num1,num2))
    if op=="E":
        global exit
        exit = True
def menu():
    global num1
    global num2
    global exit
    num1= int(input("Introduce un numero: "))
    num2=int(input("Introduce otro numero: "))
    while not exit:
        print("A: Suma\nB: Resta\nC: Multiplicación\nD: Division\nE: Salir")
        op=input("Opcion-> ")
        switch(op)
menu()