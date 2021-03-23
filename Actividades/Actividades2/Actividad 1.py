# Atributes
TIPOA="A"
TIPOB="B"
PRECIOA=100
PRECIOB=200
TAMAÑO1="1"
TAMAÑO2="2"
# Definitions/Methods
def calculoPrecio(tipo,tamaño,cantidad):
    precio=0
    plus=0
    if tamaño==TAMAÑO1 or tamaño==TAMAÑO2 and tipo==TIPOA or tipo==TIPOB:
        if tipo==TIPOA:
            precio=PRECIOA
        elif tipo==TIPOB:
            precio=PRECIOB

        if tamaño==TAMAÑO1 and tipo==TIPOA:
            plus=20
        elif tamaño==TAMAÑO2 and tipo==TIPOA:
            plus=30
        elif tamaño==TAMAÑO1 and tipo==TIPOB:
            plus=-30
        elif tamaño==TAMAÑO2 and tipo==TIPOB:
            plus=-50
    else:
        raise ValueError("Tipo o Tamaño incorrectos")
    precioFinal= (precio+plus)*cantidad
    return precioFinal
def main():
    print("Venta de Uvas")
    tipo=input("Selecciona un tipo(A/B): ")
    tamaño=input("Selecciona un tamaño(1/2):")
    cantidad=int(input("Selecciona una cantidad: "))
    precioFinal=calculoPrecio(tipo,tamaño,cantidad)
    print("Total a pagar es de "+str(precioFinal)+"€")

main()