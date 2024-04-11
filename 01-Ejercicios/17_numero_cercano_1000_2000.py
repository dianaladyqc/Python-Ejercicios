def cercania(n):
    return (abs(1000-n)<100) or (abs(2000-n)<100)

print(cercania(1000))
print(cercania(950))
print(cercania(200))

print()

print(cercania(2000))
print(cercania(1950))
print(cercania(3200))