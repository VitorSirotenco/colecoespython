#CONJUNTOS SAO MUTAVEIS A MENOS QUE USE O FROZENSET

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()#pra fazer uma copia raza da lista
assistiram.extend(usuarios_machine_learning) #pra colocar a lista dentro da variavel

print(assistiram)# sai com os numeros repetidos das duas listas

print(set(assistiram))#colocando dentro de um conjunto (set) ele tira os numeros repetidos


#operações de conjuntos

usuarios_alura = {16, 24, 44, 57}
usuarios_udemy = {14, 24, 57, 43}

estudantes = usuarios_udemy | usuarios_alura #OU INCLUSIVO
print(estudantes)

alunos = usuarios_udemy & usuarios_alura # E, quem fez os dois
print(alunos)

aprendiz = usuarios_udemy ^ usuarios_alura # OU EXCLUSIVO
print(aprendiz)

mestre = usuarios_udemy - usuarios_alura # menos quem
print(mestre)

usuarios_alura.add(15) #o metodo append não funciona com conjuntos






