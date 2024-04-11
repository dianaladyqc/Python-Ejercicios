def generar_numeros_pares(n=100):
    pares=[]
    contador =0
    numero=0
    while contador<n:
        if numero%2==0:
            pares.append(numero)
            contador+=1
        numero +=1
    return pares

n=int(input('escriba la cantidad de numeros pares positivos a generar: '))
if n>0:
    p=generar_numeros_pares(n)
    print(p)
    print('cantidad de pares: ', len(p))
else:
    print('el numero debe de ser positivo')
