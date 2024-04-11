def producto_cadena(cadena,repeticion):
    resultado=""
    for i in range(repeticion):
        resultado+=cadena
    return resultado

print('Python'*3)
print(producto_cadena('cadena',3))