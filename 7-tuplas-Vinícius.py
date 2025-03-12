
minha_tupla = (100,10,20,30,40)
numero = minha_tupla
print(minha_tupla[0])
menor = min(minha_tupla)
print(menor)
menor1 = max(minha_tupla)
print(menor1)
menor2 = len(minha_tupla)
print(menor2)
menor3 = sum(minha_tupla)
print(menor3),
menor4 = sort(minha_tupla)
print(menor4)
menor5 = sorted(minha_tupla)
print(menor5)

tupla = (1,2,3,4,5)
1 = [1,2,3,4,5]
a,b,c,d,e = 1   
print(1)
tupla


conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

# União
uniao = conjunto1 | conjunto2  # ou conjunto1.union(conjunto2)
print(uniao)  # Saída: {1, 2, 3, 4, 5, 6}

# Interseção
intersecao = conjunto1 & conjunto2  # ou conjunto1.intersection(conjunto2)
print(intersecao)  # Saída: {3, 4}

# Diferença
diferenca = conjunto1 - conjunto2  # ou conjunto1.difference(conjunto2)
print(diferenca)  # Saída: {1, 2}

# Diferença simétrica
dif_simetrica = conjunto1 ^ conjunto2  # ou conjunto1.symmetric_difference(conjunto2)
print(dif_simetrica)  # Saída: {1, 2, 5, 6}

# Verificar subconjunto
print({1, 2}.issubset(conjunto1))  # Saída: True
print(conjunto1.issuperset({1, 2}))  # Saída: True



# Criando um conjunto com chaves {}
conjunto1 = {1, 2, 3, 4, 5}
print(conjunto1)  # Saída: {1, 2, 3, 4, 5}

# Criando um conjunto com a função set()
conjunto2 = set([1, 2, 3, 4, 5])
print(conjunto2)  # Saída: {1, 2, 3, 4, 5}

#Adicionando Elementos
#Para adicionar elementos a um conjunto, utilize o método add().


conjunto = {1, 2, 3}
conjunto.add(4)
print(conjunto)  # Saída: {1, 2, 3, 4}

#Removendo Elementos
#Para remover um elemento de um conjunto, utilize os métodos remove() ou discard(). A diferença entre eles é que remove() gera um erro se o elemento não estiver presente no conjunto, enquanto discard() não gera erro.


conjunto = {1, 2, 3, 4}
conjunto.remove(3)
print(conjunto)  # Saída: {1, 2, 4}

conjunto.discard(2)
print(conjunto)  # Saída: {1, 4}

conjunto.discard(5)  # Não gera erro se o elemento não existir
print(conjunto)  # Saída: {1, 4}


form_user = {


 'nome':None,
 'idade':None,
 'endereço':None,
 'cursos': 0


}



nome1 = input('nome:')
endereco1 = input('endereco:')
cursos1 = input('cursos:')
cursos2 = input('cursos:')
cursos3 = input('cursos:')
lista_cursos = []
lista_cursos +=(cursos1, cursos2,cursos3 )



form_user['nome'] =  nome1
form_user['idade'] =  idade1
form_user['endereço'] =  endereco1
form_user['cursos'] =  lista_cursos


print(form_user)

loja = {
'fone':349.90,
'livro':99.90,
'tablet':2000
}

prod1 = input("digite o produo:")
prod2 = input("digite o produo:")
prod3 = input("digite o produo:")
prod4 = input("digite o produo:")

lista_prod = []
lista_valores = []

lista_prod.extend([prod1,prod2,prod3,prod4])
lista_valores +=(loja[prod1], loja[prod2], loja[prod3], loja[prod4])

soma = sum(lista_valores)
print('Produtos:', lista_prod)
print('...'*2)
print('R$', soma)
