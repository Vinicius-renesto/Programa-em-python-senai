# Exercício 0: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.
lista = list(range(2,20,2))
print(lista)

# Exercício 1: Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.
lista_1 = [1,2,3,4,5,6,7,8,9,10]
print(lista_1)

# Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.
imprimir = lista_1[2]
print(imprimir)

# Exercício 3: Adicione o número 9 à lista numeros e imprima a lista atualizada.
lista_1.append(9)
print(lista_1)

# Exercício 4: Remova o número 5 da lista numeros e imprima a lista resultante.
lista_1.remove(5)
print(lista_1)

# Exercício 5: Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o resultado.
lista_2 = [ 'ferrari','bugatti','lamborghini' ]
lista_3 = lista_1 + lista_2
print(lista_3)