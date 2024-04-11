def crear_histograma(lista, caracter='*'):
    for e in lista:
        print(caracter*e)
        # for i in range(e):
        #     print(caracter,end='')
lista = [2,1,3,6,9]
crear_histograma(lista)
