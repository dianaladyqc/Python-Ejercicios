def suma_numeros(a,b,c):
    suma=a+b+c
    if a==b and a==c:
        suma*=3
    return suma
print(suma_numeros(2,2,7))
print(suma_numeros(2,2,2))
