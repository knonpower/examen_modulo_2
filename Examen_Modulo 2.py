def iniciar_abaco():
    top = "+--+"
    bar = "|  |"
    barra = top
    for i in range(0,10):
        barra = barra = "/n" +bar
    barra + "/n" +top
    return barra

def descomponer_numero(...):
    pass

def agregar_puntos_a_numeros(numero):

print(iniciar_abaco())

if __name__ == "__main__":
    iniciar_abaco()
    while True:
        interrogar_usuario()
        llenar_abaco()     