# Importação das bibliotecas por motivos de organização no código e legibilidade.
import time
import os

opcao = -1 # Valor lógico inicial do usuário.

# Usuário e saldo.
user = "Lucas"
balance = 0

# Arrays onde armazena um histórico de depósito e saques.
deposit_arr = []
withdraw_arr = []

# Controle de saques por dia.
withdraw_log = 0 # Valor inicial.
WITHDRAW_LIMIT = 2 # Valor limite.

while opcao != 4: 

    # Boas vindas + menu de opções para usuário
    opcao = int(input(f"Bem vindo {user}, ao sistema bancário DinDinhos! Preciso que informe o que deseja fazer. \n\n [1] Sacar \n [2] Depósito \n [3] Puxar extrato \n [4] Sair \n\nInsira o valor de acordo com as opções acima: "))
    print(" ")
    print(f"Saldo atual: R${balance:.2f}") # Indicação do saldo
    print(" ")

    if opcao == 1: 
       withdraw = float(input(f"Digite quanto deseja sacar deste valor: R$")) # Armazena o valor do saque
       print(" ")

       if balance == 0 or withdraw <= 0 or withdraw > balance: 
           # Caso o saldo seja 0 ou o valor do saque seje negativo ou o saque maior que o saldo, não terá continuação.
           print(f"Sacando o valor de R${withdraw:.2f}...")
           time.sleep(3)
           print(" ")
           print(f"Erro no saque! O valor é inválido. \n\nValor disponível R${balance:.2f}")
           print(" ")

           time.sleep(4) # Delay
           os.system("cls") # Limpa o terminal em execução.
       elif withdraw <= balance: # Caso o saque seja menor que o saldo ou igual, é possível realizar o saque.
          print(f"Realizando o saque. . .")
          print(" ")

          time.sleep(3)

          if withdraw_log > WITHDRAW_LIMIT: # Já aviso ao interpretador que caso passar o limite, retorne um bloqueio de saques.
               print("Não é possível realizar mais operações de saque, foi excedido o limite de saques diários. Retorne em até 24h.")
          else: 
               print(f"Saque de R${withdraw:.2f} realizado com sucesso!")
               print(" ")

               balance = balance - withdraw # Calcula o saldo - o valor do saque = saldo
               withdraw_log = withdraw_log + 1 # Consto cada saque a quantidade de vezes que foi sacado
               withdraw_arr.append(withdraw)
               # Caso contrário, o saldo é subtraído e armazenado no array.

          print("Voltando ao Menu de operação do sistema...")
          print(" ")

          time.sleep(3)
          os.system("cls")
    elif opcao == 2:
       deposit_value = float(input("O quanto deseja depositar na sua conta? R$")) # Valor do depósito armazenado.
       print(" ")

       if deposit_value >= 1:
          print("Depositando. . .")
          balance = balance + deposit_value # Calcula o saldo somando com o valor do depósito.
          print(" ")

          time.sleep(3)
          print(f"Depósito realizado! Seu saldo foi alterado com sucesso. \n\nSaldo atual R${balance:.2f}")
          # Indica valor atual do saldo do cliente após o depósito.
          print(" ")

          deposit_arr.append(deposit_value) # Armazena a variável do valor do depósito no array.  

          time.sleep(4)
          os.system("cls")
       else:
          print("Depositando. . .")
          time.sleep(3)
          print(" ")

          time.sleep(3)
          print("Valor inválido! Insira um valor válido para depósito.")

          time.sleep(5)
          os.system("cls")
    elif opcao == 3:
        if withdraw_arr == [] and deposit_arr == []: # Se ambos arrays forem vazios, retorna uma mensagem.
          
          print("Processando o extrato. . .")
          time.sleep(3)
          print(" ")
          print("Extrado realizado! Mas pelo que pude ver é a primeira vez de você sacando por aqui e também não há depósitos algum, que tal realizar um saque ou depósito?")
        else: 
           print("############ Extrato realizado com sucesso! ############") # Caso contrário, retorna todo o extrato
           print(" ")

           if withdraw_arr != []: # Método onde para cada valor dentro do array seja salvo e constado dentro da String
              for W_log in withdraw_arr:
                 print(f"Saque de R${W_log:.2f} realizado com sucesso!")

           if deposit_arr != []:
              for D_log in deposit_arr:
                 print(f"Depósito de R${D_log:.2f} realizado com sucesso!")
        
        print(" ")
        time.sleep(6)
        print("Retornando ao menu...")

        print(" ")
        time.sleep(3)
        os.system("cls")
    elif opcao == 4:
       print("Obrigado por preferir nosso sistema, até mais!") # Caso cliente escolha a opção de sair, encerre o sistema.
       break
    else: # Caso qualquer outro tipo de caractere que não seja o que decide a opção, e finaliza o sistema.
       print("Obrigado por preferir nosso sistema, até mais!")
       break