def problema():
    print('X+5=10 \n¿Cuánto vale X?')

def verficar_respuesta(x):
    if x+5==10:
        print('Es correcto!')
    else:
        print('Vuelve a intentar')

problema()
x = int(input())
verficar_respuesta(x)