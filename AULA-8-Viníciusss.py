#Peça para o usuário digitar um número, verifique se um número é positivo, negativo ou zero.
'''numero = float (input('fale um número ? '))
if numero ==  0 :
    print('seu valor é zero')
elif numero > 0 :
    print('seu valor é positivo ')
elif numero < 0 :
    print('seu valor é negativo')'''

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com base na idade.
'''numero1 = float(input('fale sua idade ? '))
if numero1 >= 18 :
    print('pode votar')
elif numero1 < 18 :
    print ('você nao tem idade para votar') ''' 

# Declara uma variável com um número qualquer, determine se um número é par ou ímpar.
'''n  = 10
if n % 2 == 0:
    print('Par')
else:
    print('impar') 
'''

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo é equilátero, isósceles ou escaleno
'''a = int(input('Digite um numero '))
b = int(input('Digite um numero '))
c = int(input('Digite um numero '))

if a == b == c:
   print('equilatero') 
elif a == b and  b!= c  or  a== c and b != c:
  print('isoceles') 
else:
  print('escaleno')'''

# Determine se um número é múltiplo de 5 e 7.
'''n = 35
if n% 5 == 0 and n% 7 == 0 :
    print('é multiplicado')
else :
    print('não é multiplicado')'''

# Verifique se um número é positivo e maior que 10
'''n1  =  int(input())
if  n1 > 0 and n1 >10:
    print('é esse o numero')  
else: 
    print('Não é')'''

# Verifique se um número é divisível por 3 ou 5.
'''n2 =  int(input('Digite um numero'))
if n2 % 3 ==0 or n2 % 5 ==0: 
    print('Divisivel')
else:
    print('Não é ')'''



# Desafio 1


'''livro = 99,90
tablet = 1999,99
fones = 349,90

lista_consumos ={ livro: 1 ,tablet : 2 ,fones : 3 }


print('olá, bem vindo a amazon')
decisão = input('voçê deseja fazer alguma compra ?')
if decisão == 'sim':
    print('otimo,entao vamos começar, mas antes da compra preciso que preencha algumas informações, para registro de compras')
    nome1 = input('nome:')
    idade1 = input('idade:')
    CPF1= input('CPF')
    email1= ('email')
    telefone1= float (input('telefone'))
    print('OK, tenha uma otima compra', nome1)
    consumos = (lista_consumos)
    if consumos == 'livros':
        quantidades = float(input('quantos livros voçê quer ? (limite até 3 livros por compra)'))
    elif quantidades == 1 :
            reultado = float(print('o valor é', livros))
    elif quantidades == 2 :
            reultado1= float(print('o valor é', livros * 2 ))
    elif quantidades == 3 :
            reultado2= float(print('o valor é', livros * 3 ))
    if consumos == 'tablet':
      quantidades1 = float(input('quantos livros voçê quer ? (limite até 3 livros por compra)'))
    elif quantidades1 == 1 :
            reultado3= float(print('o valor é', tablet))
    elif quantidades1 == 2 :
            reultado4= float(print('o valor é', tablet * 2 ))
    elif quantidades1 == 3 :
            reultado5= float(print('o valor é', tablet * 3 ))
    if consumos == 'fones':
      quantidades2 = float(input('quantos livros voçê quer ? (limite até 3 livros por compra)'))
    elif quantidades2 == 1 :
            reultado3= float(print('o valor é', fones))
    elif quantidades2 == 2 :
            reultado4= float(print('o valor é', fones * 2 ))
    elif quantidades2 == 3 :
            reultado5= float(print('o valor é', fones * 3 ))
else :
    print('ok, obrigado pela atenção')'''






'''nome_cliente = input('Digite o nome do Cliente 1: ')
idade_cliente = int(input('Digite a idade do Cliente 1: '))

nome_cliente1 = input('Digite o nome do Cliente 2: ')
idade_cliente1 = int(input('Digite a idade do Cliente 1: '))

nome_cliente2 = input('Digite o nome do Cliente 3: ')
idade_cliente2 = int(input('Digite a idade do Cliente 1: '))


print('Tipos de Quarto: Simples, Duplo, Luxo')

quarto_cliente = input('Escolha o quarto para o Cliente 1: ')
quarto_cliente1 = input('Escolha o quarto para o Cliente 2: ')
quarto_cliente2 = input('Escolha o quarto para o Cliente 3: ')


simples = 100
duplo = 150
luxo = 250

dias_cliente = int(input(f'Quantos dias o Cliente 1 ({nome_cliente}) ficará hospedado? '))
dias_cliente1 = int(input(f'Quantos dias o Cliente 2 ({nome_cliente1}) ficará hospedado? '))
dias_cliente2 = int(input(f'Quantos dias o Cliente 3 ({nome_cliente2}) ficará hospedado? '))


if quarto_cliente == 'simples':
    valor_cliente1 = simples * dias_cliente
elif quarto_cliente == 'duplo':
    valor_cliente1 = duplo * dias_cliente
else:
    valor_cliente1 = luxo * dias_cliente

if quarto_cliente1 == 'simples':
    valor_cliente2 = simples * dias_cliente1
elif quarto_cliente1 == 'duplo':
    valor_cliente2 = duplo * dias_cliente1
else:
    valor_cliente2 = luxo * dias_cliente1

if quarto_cliente2 == 'simples':
    valor_cliente3 = simples * dias_cliente2
elif quarto_cliente2 == 'duplo':
    valor_cliente3 = duplo * dias_cliente2
else:
    valor_cliente3 = luxo * dias_cliente2


print(f'Cliente 1: {nome_cliente}, {dias_cliente} anos, Quarto {quarto_cliente}, {dias_cliente} dias')
print(f'Valor Total Cliente 1: R$ {valor_cliente1:.2f}')

print(f'Cliente 2: {nome_cliente1}, {dias_cliente1} anos, Quarto {quarto_cliente1}, {dias_cliente1} dias')
print(f'Valor Total Cliente 2: R$ {valor_cliente2:.2f}')

print(f'Cliente 3: {nome_cliente2}, {dias_cliente2} anos, Quarto {quarto_cliente2}, {dias_cliente2} dias')
print(f'Valor Total Cliente 3: R$ {valor_cliente3:.2f}')'''