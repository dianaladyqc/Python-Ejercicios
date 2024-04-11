def Replica(cadena, n):
    n_caracteres=n
    if n_caracteres>len(cadena):
        n_caracteres=len(cadena)
    subcadena=cadena[n_caracteres]
    resultado=''
    for i in range(n):
        resultado+=subcadena
    return resultado
print(Replica('Python',6))
print(Replica('ana',4))
print(Replica('carlos',1))
