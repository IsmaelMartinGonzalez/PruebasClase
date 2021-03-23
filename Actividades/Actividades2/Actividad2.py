# Atributes
PRECIO1=65
PRECIO2=70
PRECIO3=95
PRECIO4=115
PAUTOBUS=4000
# Definitions/Methods
def calculoImportePorAlumno(totalA):

    importeBusporA=PAUTOBUS/totalA
    if totalA>=100:
        importeFinal=importeBusporA+PRECIO1
    elif totalA<=99 and totalA>=50:
        importeFinal=importeBusporA+PRECIO2
    elif totalA<=49 and totalA>=30:
        importeFinal=importeBusporA+PRECIO3
    else:
        importeFinal=importeBusporA+PRECIO4

    return importeFinal
def calculoImporteAgencia(totalA):
    if totalA>=100:
        precioPorA=PRECIO1*totalA
    elif totalA<=99 and totalA>=50:
        precioPorA=PRECIO2*totalA
    elif totalA<=49 and totalA>=30:
        precioPorA=PRECIO3*totalA
    else:
        precioPorA=PRECIO4*totalA

    importeFinal=PAUTOBUS+precioPorA
    return importeFinal
def main():
    alumos=int(input("Total de alumno que van al viaje: "))
    importePorA=calculoImportePorAlumno(alumos)
    totalApagar=calculoImporteAgencia(alumos)
    print("Total a pagar a la agencia: "+str(totalApagar)+"€, importe por alumno: "+str(importePorA)+"€")
main()