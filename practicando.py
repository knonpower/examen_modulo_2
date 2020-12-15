
def monto():    
    monto = int(input('ingrese Monto: '))
    montos = [20000,10000,5000,500,100,50]
    for i in montos:
        if monto >= i:
            sobrante =  monto // i
            print("existen " + str(sobrante) + " ficha de "+ str(i) + " colores")
            monto = monto % i


def iniciar_abaco():
    top = "+--+"
    bar = "|  |"
    barra = top
    for i in range(0,10):
        barra = barra + "\n"+bar
        barra = barra + "\n" + top
        return barra

print(iniciar_abaco())
