def problema():
    print('X+5=10 \nEscribe tu respuesta a continuación\n¿Cuánto vale X?')

def verficar_respuesta(x):
    while x+5!=10:
        int(input('Intentalo de nuevo:   ')) 
    else:
        print('Felicidades')

problema()
x = int(input())
verficar_respuesta(x)