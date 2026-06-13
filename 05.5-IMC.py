#variaveis do peso e altura do mlk

peso = float(input("Fala o seu peso: "))
altura = float(input("Fala a sua altura: "))
#calculando o IMC

imc = peso / (altura * altura)
print("o seu IMC é:", imc)
#ta ok?
if imc >= 30:
        print("cuidado com a saude, se cuida")
elif imc < 30:
        print("ta tudo ok, continue assim")
else:
        print("ok?")


#condições do IMC
if imc <= 18.5:
    print("Abaixo do peso: Grau 0")
elif imc <= 24.9:
    print("Peso normal: \nGrau 0")
elif imc <= 29.9:
    print("Sobrepeso: \nGrau 0")
elif imc <= 34.9:
    print("Obesidade Grau I: \nGrau 1")
elif imc <= 39.9:
    print("Obesidade Grau II: \nGrau 2")
else:
    print("Obesidade Grau III: \nGrau 3")