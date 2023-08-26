idades = [15,17,31,23,50]

for idade in idades:
    print(idade)

if 15 in idades:
    print('possui esse elemento')
else:
    print('nao possui esse elemento')

idades.append(32) #adiciona um elemento ao final da lista
print(idades)

idades.insert(3, 5) #primeiro parametro é a posição e o segundo o elemento
print(idades)

idades.extend([25,39,41]) #esse metodo adiciona uma lista dentro de outra lista
print(idades)

idades_ano_que_vem = []
for idade in idades:
    idades_ano_que_vem.append(idade + 1)

print('Idades ano que vem: ', idades_ano_que_vem)

idades_ano_que_vem = [(idade + 1) for idade in idades] #jeito mais simplificado de fazer
print('Idades ano que vem: ', idades_ano_que_vem)

maior_idade = [(idade) for idade in idades if idade > 18]
print(maior_idade)


def proximo_ano(idade):
    return idade + 1

ano_que_vem = [proximo_ano(idade) for idade in idades] # funcao dentro do array
print(ano_que_vem)

