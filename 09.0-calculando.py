#Feito por: 01001010 01101111 11000011 01101111 00100000 01001100 01110101 01100011 01100001 01110011
# calculando o IMC


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")
if imc >= 30:
    print("Cuidado com a saude")
if imc < 30:
    print("Tudo ok")

if imc < 18.5:
    print("Abaixo do peso")
if imc >= 18.5 and imc < 24:
    print("Peso normal")
if imc >= 24 and imc < 29.9:
    print("Sobrepeso")
if imc >= 30 and imc < 34.9:
    print("Obesidade Grau I")
if imc >= 35 and imc < 39.9:
    print("Obesidade Grau II")
if imc >= 40:
    print("Obesidade Grau III (Mórbida)")   