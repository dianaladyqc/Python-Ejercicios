from random import randint
numeros_aleatorios=[randint(1,100) for _ in range(50)]
print(numeros_aleatorios)
numeros_impares=filter(lambda n: n%2==1, numeros_aleatorios)
print()
print(list(numeros_impares))



def encontrar_impares(lista):
    impares=[]
    for i in lista:
        if i%2==1:
            impares.append(i)
    return impares
print(encontrar_impares(numeros_aleatorios))
