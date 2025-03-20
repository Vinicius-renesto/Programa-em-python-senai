# ***1*** 

# ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***




# def comparar():
#     n1 = 11
#     n2 = 1
#     if n1 % 2 == 0 and n2 % 2 ==0:
#         print('ambos são pares')
#     elif n1 % 2 == 0 or n2 % 2 ==0:  
#         print('um dos dois é par')
#     else:
#         print('nenhum é par')    

# comparar()



# ***2***

# ***CRIE UM AFUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***


# def mult():
#     print(3*5*4)

# mult()    





# ***3***

# ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADo DE UM NÚMERO.***


# def elevado():
#     n = int(input('número:'))
#     el = int(input('elevado:'))
#     result_elevado = n ** el
#     print(result_elevado)

# elevado()


# ***4***

# ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM 
# PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS***
# def verificar():
#     idade  =  int(input('idade:'))
#     if idade ==18:
#         print('Você tem 18 anos')
#     else:
#         print('Não tem 18 anos')    
# verificar()

# ***5***

# ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***


# def descobrir():
#     ano_nasc  =  int(input('ano de nascimento:'))
#     mes = int(input('Digite o mês de nascimento numero:'))
#     mes_atual = int(input('Digite o mês atual:'))
#     ano  = 2025
    
#     if mes <= mes_atual:
#         idade = ano -  ano_nasc
#         print(idade)
#     else:
#          idade = (ano-1) -  ano_nasc
#          print(idade)

# descobrir()    



# ***6***

# ***DESENVOLVA UM AFUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999***


# def verificar():
#     anos_lista = [1998,1994,1962,2002, 1958]
#     ano = int(input('Ano: '))
#     if ano in anos_lista:
#         print('O Brasil ganhou esse ano')
#     else:
#         print('O Brasil não ganhou esse ano')    

# verificar()
# ***7*** 

# ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***


def restaurante():
    restau = {
      'salada':50.,
      'macarronada':100,
      'sanduiche':30,
      'sorvete':40
     
    }
    valor_cliente = []
    prod_cliente = []
    p =  input('Deseja fazer o pedido? ')
    while p == 's':
          escolha  =  input('Digite o seu produto: ')
          prod_cliente.append(escolha)
          valor_cliente.append(restau[escolha])
          print(prod_cliente)
          print('R$', valor_cliente)
          soma =  sum(valor_cliente)
          print('***'*10)
          print('TOTAL: R$',soma)
          p =  input('Deseja fazer o pedido? ')
    else:
        print('obrigada volte sempre!')      

restaurante()
