#Criando as variaveis
nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua idade? "))


#verificando a condição da idade
if idade >= 18:
    possui_carteira = input("Possui carteira de motorista? \n (1-sim / 2-Não)")
    if possui_carteira == "1":
       print("Pode dirigir")
    else:
       print("Pode não man.")

else:
    print("menor de idade")