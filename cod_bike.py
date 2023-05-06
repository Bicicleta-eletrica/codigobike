usuarios=[]
senhas=[]

from getpass import getpass
from hashlib import sha256

while True:
    opcao=input("Pressione 1 para acessar sua conta, 2 para criar uma conta ou 3 para sair: ")

    if int(opcao) == 1:
        usuario=input("Insira o usuário: ")
        senha=getpass(print("Insira sua senha: "))
        senha=sha256(senha.encode()).digest()
        if usuario in usuarios and senha in senhas:
            print("Conectado com sucesso!")
        else:
            print("Usuário ou senha inválidos, tente novamente.")
    

    
    elif int(opcao) == 2:
        print("Cadastre seu usuário e senha")
        
        usuario=str(input("Insira seu usuário: "))
        if usuario in usuarios:
            print("Usuario existente, tente outro!")
        else:
            usuarios.append(usuario)
        
            senha=getpass(print("Insira sua senha: "))
            senha=sha256(senha.encode()).digest()
            senhas.append(senha)
            print("Conta criada com sucesso!")


    elif int(opcao) == 3:
        print("Obrigado por acessar!")
        break
    

    else: 
        print("Opção Inválida, tente novamente")

with open('usuarios.txt','w') as arq_users:
  for user in usuarios:
    arq_users.write(user)
    arq_users.write('\n')

with open('senhas.txt','w') as arq_senhas:
  for sen in senhas:
    arq_senhas.write(str(sen))
    arq_senhas.write('\n') 