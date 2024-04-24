# Dado n, toma la suma de los dígitos de n. 
# Si ese valor tiene más de un dígito, continúe 
# reduciendo de esta manera hasta que se produzca un número de un solo dígito. La entrada será un número entero no negativo.
def digital_root(n):    
    if n<10:
        return n
    else:
        suma=n//10+n%10
        return digital_root(suma)