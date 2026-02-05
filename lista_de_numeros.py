for value in range(1,21):
    print(value)

#for value in range(1,1_000_001):
#    print(value)

numeros = [1,1_000_000]
print(sum(numeros))
print(min(numeros))
print(max(numeros))

for value in range(0,21,3):
    print(value)

multiplos_de_3 = []
for value in range(3,31,3):
    multiplos_de_3.append(value)
print(multiplos_de_3)

ao_cubo = []
for numero in range(1,11):
    elevado3 = numero ** 3
    ao_cubo.append(elevado3)
print(ao_cubo)

ao_cubo = [numero ** 3 for numero in range(1,11)]
print(ao_cubo)