def es_vocal(v):
    if len(v)==1:
        vocales='aeiou'
        #convertimos la entrada a minuscula
        v=v.lower()
        return v in vocales
    else:
        return False

print(es_vocal('a'))
print(es_vocal('L'))
print(es_vocal('A'))
print(es_vocal('p'))
print(es_vocal('ñ'))
print(es_vocal('ae'))