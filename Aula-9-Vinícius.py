'''# Atividade 1 (exercicio 1)
c = 0
while c >= 0   :
   if c <= 1000 :
    print(c)
    c =+ (c + 1 )
   else :
    break    

# Atividade 1 (exercicio 2)
lista_nomes = []
nomes = 0
while nomes >= 0 :
    if nomes <= 9 :
      nome = input('qual seu nome ? ')
      nomes =+ (nomes + 1 )
      lista_nomes.append (nome)
    else :
     break  

    print(lista_nomes)
'''
# Atividade 2 

lista_cadastro = []
cadastro = input('você deseja fazer um cadrastro ?')
if cadastro == 'sim' :
    email_usuario = input('qual seu email ?')
    senha_usuario = input('qual seu senha ?')
    lista_cadastro.append (email_usuario)
    lista_cadastro.append (senha_usuario)
    print('seu email é',email_usuario,'e sua senha é',senha_usuario)
    login = 0 
    while login >= 0 :
       if login <= 3 :
        email_usuario = input('qual seu email ?')
       if email_usuario == lista_cadastro :
         print('correto')
       else :
          print('verifique seu email')
       senha_usuario = input('qual seu senha ?')   
       if senha_usuario == lista_cadastro :
         print('correto')
       else :
          print('verifique sua senha')
          lista_notas = []
       for notas in range(3 ):
        notas = float(input('qual sua nota ?'))
        lista_notas.append (notas)
        soma =  sum(lista_notas)
        print(soma)
        me = soma/len(lista_notas)
        print(me)
        break


    else :
       print ('tente novamente')

else :
    print('obrigado pela atenção')

