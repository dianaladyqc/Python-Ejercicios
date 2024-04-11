base=None
altura=None

while True:
    try:
        base=float(input('base del triangulo: '))
        break
    except: # expresion as identifier:
        print('Debe escribir un numero')

while True:
    try:
        altura=float(input('altura del triangulo: '))
        break
    except: # expresion as identifier:
        print('Debe escribir un numero')

area=base*altura/2
print('el area del triangulo es: ', area)