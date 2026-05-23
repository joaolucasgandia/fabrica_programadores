#coisando coisas
nome_produto = input("Digite o nome do produto: ")
preco = float(input("digite o preço: "))
valor_desconto = float(input("digite o valor do desconto: "))
desconto = float(input("digite o desconto: "))

preco_desconto = preco - preco * desconto / 100
preco_final = preco_desconto - valor_desconto

print(f"produto: {nome_produto} - Preço final: R${preco_final}")s
