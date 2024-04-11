print(5 in [1,2,5,6,9,47])
print('k' in 'Fork')
print('a' in 'Fork')

def pertenece(lista, elemento):
    for i in lista:
        if elemento==i:
            return True
    return False

print(pertenece((2,3,6,5,8),5))
print(pertenece([5,6,8,5],2))
print(pertenece('Fork','k'))
print(pertenece('Fork','o'))
print(pertenece(['4','k','g'],'g'))