from datetime import datetime
import os

while True:
  print('''Cadastro de pessoas
  1 - Iniciar Cadastro
  2 - Procurar Pessoas
  3 - Encerrar programa''')
  opc = int(input("Digite uma opção: "))
  if opc == 1:
    
    while True:
      try:
        nome = input("Digite seu nome: ")
        int(nome)
        print("Digite um nome válido")
      except ValueError:
        break    
    while True:
      try:
        cpf = str(input("Digite seu cpf: "))
        if len(str(cpf))==11:
          break
        else:
          print("cpf inválido!")
      except ValueError:
        print("Digite somente números!")
    while True:
      try:
        rg = int(input("Digite seu rg: "))
        if len(str(rg)) >2 and len(str(rg))<14:
          break
        else:
          print("rg inválido!")
      except ValueError:
        print("Digite somente números!")
    while True:
      try:
        nasc = str(input("Digite sua data de nascimento: "))
        datetime.strptime(nasc, '%d/%m/%Y')
        break
      except ValueError:
        print("Digite uma data válida (DD/MM/AAAA)!")
    while True:
      try:
        sexo = input("Digite seu sexo: ")
        int(sexo)
        print("Digite um sexo válido")
      except ValueError:
        break
    while True:
      try:
        tel = int(input("Digite seu telefone: "))
        if len(str(tel))==11:
          break
        else:
          print("telefone inválido!")
      except ValueError:
        print("Digite somente números!")
    while True:
      try:
        endereco = input("Digite seu endereço: ")
        int(endereco)
        print("Digite um Endereço válido")
      except ValueError:
        break
    while True:
      try:
        num = int(input("Digite seu número da casa: "))
        if len(str(num))>0 and len(str(num))<6:
          break
        else:
          print("número inválido!")
      except ValueError:
        print("Digite somente números!")
    while True:
      try:
        comp = input("Digite seu complemento: ")
        int(comp)
        print("Digite um complemento válido")
      except ValueError:
        break
    while True:
      try:
        cep = int(input("Digite seu cep: "))
        int(cep)
        if len(str(cep))==8:
          break
      except ValueError:
        print("Digite somente números!")
    while True:
      try:
        bairro = input("Digite seu bairro: ")
        int(bairro)
        print("Digite um bairro válido")
      except ValueError:
        break
    while True:
      try:
        cidade = input("Digite sua cidade: ")
        int(cidade)
        print("Digite uma cidade válida")
      except ValueError:
        break
    while True:
      try:
        UF = input("Digite sua UF: ")
        int(UF)
        print("Digite uma UF válida")
      except ValueError:
        break
    while True:
      try:
        email = input("Digite seu email: ")
        int(email)
        print("Digite um email válido")
      except ValueError:
        break
    while True:
      try:
        nomePai = input("Digite o nome de seu pai: ")
        int(nomePai)
        print("Digite um nome válido")
      except ValueError:
        break
    while True:
      try:
        nomeMae = input("Digite o nome de sua mãe: ")
        int(nomeMae)
        print("Digite um nome válido")
      except ValueError:
        break
    novo_ser = (f"nome: {nome}",f"cpf: {cpf}", f"RG: {rg}",f"Data de Nascimento: {nasc}",f"Sexo:{sexo}",f"Telefone: {tel}",f"Email:{email}", f"Endereço:{endereco}",f"Número:{num}",f"Complemento:{comp}",f"Bairro:{bairro}",f"CEP: {cep}",f"Cidade: {cidade}",f"UF: {UF}",f"Nome do Pai: {nomePai}",f"Nome da Mãe: {nomeMae}")
    nome_do_arquivo = nome
    with open(f"{nome_do_arquivo}.txt",'w') as arquivo:
      for i in novo_ser:
        arquivo.write(str(i)+'\n')
    
  elif opc == 2:
    while True:
      Dados = str(input("Digite um nome do usuário que deseja buscar: "))
      if os.path.exists(f"{Dados}.txt"):
        with open(f"{Dados}.txt",'r') as arquivo:
          for i in arquivo:
            print(i)
        break
      else:
        print("Digite um usuário correto")
  elif opc == 3:
    print("Encerrar programa")
    break
  else:
    print("Digite uma opção válida")