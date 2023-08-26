idades = [15, 87, 65, 56, 32, 49, 37]

for idade in idades:
    print(idade)

print(f"o tamando da lista é: " , len(idades))

for i in range(len(idades)):
    print(i)

for i in range(len(idades)):
    print(i, idades[i])


list(range(len(idades))) # forcei a geração dos valores
print(list(range(len(idades))))

list(enumerate(idades)) #colocando dentro de uma lista as duplas

print(list(enumerate(idades)))


for indice, idade in enumerate(idades): #para desempacotar
    print(indice, idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios: # ja desempacotando e escolhendo so oq eu quero
    print(nome)


for nome, _, _ in usuarios: # tambem pode ser feito assim
    print(nome)

























