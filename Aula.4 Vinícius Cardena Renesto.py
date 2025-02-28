# comentario

# para carregar o código -> f5

# verificar qual o tipo do dado
# type()

# serve para mostra algo no ambiente de testes
# função - ação

nome = input('qual é seu nome?')
print('olá, seja bem vindo',nome)
pergunta = input('toparia calcular algumas operações?')
if pergunta == 'sim':
    print('ok vamos começar!')
    numero = input('qual é o numero?')
    numero1 = input('qual é o seu segundo numero?')
    print('soma',numero + numero1)
    
    numero2 = input('qual é o numero?')
    numero3 = input('qual é o seu segundo numero?')
    print('multiplicação',numero * numero1)
    
    numero3 = input('qual é o numero?')
    numero4 = input('qual é o seu segundo numero?')
    print('subtração',numero - numero1)
    
    numero5 = input('qual é o numero?')
    numero6 = input('qual é o seu segundo numero?')
    print('divisão',numero / numero1)

if pergunta == 'nao':
    print('ok, obrigado pela comprienção :)' )

# (*) - multiplicação
# (/) - divisão
# (+) - soma
# (-) - subtração

print('divisão:',round(div,5))
